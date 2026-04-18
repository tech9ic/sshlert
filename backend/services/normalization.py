import csv
from datetime import datetime

def load_and_normalize_alerts(filepath: str):
    alerts = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Parse timestamp into a datetime object for internal processing
                try:
                    dt = datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    dt = None
                
                alert = {
                    "timestamp_raw": row['timestamp'],
                    "timestamp": dt,
                    "device_id": row['device_id'],
                    "alert_type": row['alert_type'],
                    "severity": row['severity'],
                    "message": row['message']
                }
                alerts.append(alert)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    # Ensure sorted by time
    alerts.sort(key=lambda x: x['timestamp'] if x['timestamp'] else datetime.min)
    return alerts
