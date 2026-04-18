from typing import List, Dict
from datetime import timedelta
from backend.models.incident import Incident
from backend.services.root_cause import determine_root_cause_and_severity
from backend.config import ALERT_CATEGORIES, CORRELATION_WINDOW_MINUTES

def correlate_alerts_to_incidents(alerts: List[Dict]) -> List[Incident]:
    incidents = []
    window = timedelta(minutes=CORRELATION_WINDOW_MINUTES)
    
    # State tracking: mapping of device_id -> List of active incidents
    active_incidents_by_device = {}
    incident_counter = 1
    
    for alert in alerts:
        device = alert['device_id']
        category = ALERT_CATEGORIES.get(alert['alert_type'], "Unknown")
        
        if device not in active_incidents_by_device:
            active_incidents_by_device[device] = []
            
        matched_incident = None
        
        # Pruning loop: remove expired incidents to free memory and limit search space
        if alert['timestamp']:
            active_incidents_by_device[device] = [
                inc for inc in active_incidents_by_device[device]
                if inc.alerts[0]['timestamp'] and alert['timestamp'] - inc.alerts[0]['timestamp'] <= window
            ]
        
        # Check active incidents for this device
        for incident in active_incidents_by_device[device]:
            first_type = incident.alerts[0]['alert_type']
            first_cat = ALERT_CATEGORIES.get(first_type, "Unknown")
            
            # If both are Unknown, strictly match alert_type to prevent blending unrelated issues
            if category == "Unknown" and first_cat == "Unknown":
                if alert['alert_type'] == first_type:
                    matched_incident = incident
                    break
            elif category == first_cat:
                matched_incident = incident
                break
        
        if matched_incident:
            matched_incident.alerts.append(alert)
        else:
            new_inc = Incident(
                incident_id=f"INC-{incident_counter:03d}",
                device=device,
                start_time=alert['timestamp_raw']
            )
            new_inc.alerts.append(alert)
            incidents.append(new_inc)
            active_incidents_by_device[device].append(new_inc)
            incident_counter += 1
            
    for inc in incidents:
        inc.alerts_count = len(inc.alerts)
        if inc.alerts[0]['timestamp'] and inc.alerts[-1]['timestamp']:
            duration_secs = (inc.alerts[-1]['timestamp'] - inc.alerts[0]['timestamp']).total_seconds()
            inc.duration = f"{int(duration_secs // 60)} min"
        else:
            inc.duration = "0 min"
            
        inc.end_time = inc.alerts[-1]['timestamp_raw']
        inc.status = "Closed"
        
        cause, sev = determine_root_cause_and_severity(inc.alerts)
        inc.root_cause = cause
        inc.severity = sev
        
    return incidents
