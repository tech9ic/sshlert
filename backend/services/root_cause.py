from typing import List, Dict
from backend.config import SEVERITY_LEVELS, ROOT_CAUSE_WEIGHTS

def determine_root_cause_and_severity(alerts: List[Dict]) -> tuple[str, str]:
    if not alerts:
        return "Unknown", "Info"
        
    highest_sev_val = -1
    highest_weight_val = -1
    highest_sev_str = "Info"
    highest_cause_msg = "Unknown"
    
    for alert in alerts:
        sev_str = alert.get('severity', 'Info')
        sev_val = SEVERITY_LEVELS.get(sev_str, 0)
        
        type_str = alert.get('alert_type', 'Unknown Alert')
        weight_val = ROOT_CAUSE_WEIGHTS.get(type_str, 0)
        
        # Priority to higher severity; ties broken by logical root cause weight
        should_update = False
        if sev_val > highest_sev_val:
            should_update = True
        elif sev_val == highest_sev_val and weight_val > highest_weight_val:
            should_update = True
            
        if should_update:
            highest_sev_val = sev_val
            highest_sev_str = sev_str
            highest_weight_val = weight_val
            highest_cause_msg = type_str
            
    return highest_cause_msg, highest_sev_str
