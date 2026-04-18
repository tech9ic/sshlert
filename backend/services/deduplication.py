from typing import List, Dict

def deduplicate_alerts(alerts: List[Dict], time_window_seconds: int = 60) -> List[Dict]:
    deduped = []
    last_seen = {}
    
    for alert in alerts:
        key = (alert['device_id'], alert['alert_type'])
        
        if key in last_seen:
            last_alert = last_seen[key]
            if alert['timestamp'] and last_alert['timestamp']:
                time_diff = (alert['timestamp'] - last_alert['timestamp']).total_seconds()
                if time_diff <= time_window_seconds:
                    # Update sliding window so subsequent repeated logs roll the deduplication timer
                    last_seen[key] = alert
                    continue
        
        deduped.append(alert)
        last_seen[key] = alert
        
    return deduped
