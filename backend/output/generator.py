from backend.services.normalization import load_and_normalize_alerts
from backend.services.deduplication import deduplicate_alerts
from backend.services.correlation import correlate_alerts_to_incidents
import os

def process_pipeline():
    # 1. Base path logic
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alerts_path = os.path.join(base_dir, 'data', 'alerts.csv')
    
    # 2. Pipeline steps
    raw_alerts = load_and_normalize_alerts(alerts_path)
    total_raw = len(raw_alerts)
    
    deduped_alerts = deduplicate_alerts(raw_alerts)
    
    incidents = correlate_alerts_to_incidents(deduped_alerts)
    total_incidents = len(incidents)
    
    reduction_pct = 0
    if total_raw > 0:
        reduction_pct = round(((total_raw - total_incidents) / total_raw) * 100)
    
    # 3. Format output
    output = {
        "total_alerts": total_raw,
        "total_incidents": total_incidents,
        "reduction": f"{reduction_pct}%",
        "incidents": [inc.to_dict() for inc in incidents]
    }
    
    return output
