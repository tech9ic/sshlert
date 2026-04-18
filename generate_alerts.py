import csv
import random
from datetime import datetime, timedelta

devices = ["Router-1", "Router-2", "Switch-1", "Switch-2", "Firewall-1", "Server-DB1", "Server-Web1", "Server-APP1"]
alert_types = {
    "Network": ["Interface Down", "Packet Loss", "High Latency"],
    "Routing": ["BGP Down", "OSPF Down"],
    "System": ["CPU High", "License Expiry", "Memory Utilization High"]
}
severities = ["Info", "Warning", "Minor", "Major", "Critical"]

start_time = datetime(2026, 4, 8, 8, 0, 0)
alerts = []
current_time = start_time

# Generate about 1000 alerts grouped into burst incidents
for _ in range(80):
    incident_device = random.choice(devices)
    incident_category = random.choice(list(alert_types.keys()))
    incident_start = current_time + timedelta(minutes=random.randint(1, 15))
    current_time = incident_start
    
    # 5 to 12 alerts per group
    num_alerts = random.randint(5, 12)
    
    for _ in range(num_alerts):
        a_time = incident_start + timedelta(seconds=random.randint(0, 180)) # within 3 minutes correlation window
        a_type = random.choice(alert_types[incident_category])
        a_sev = random.choice(severities)
        message = f"Simulated threshold breached for {a_type}"
        
        alerts.append({
            "timestamp": a_time,
            "device_id": incident_device,
            "alert_type": a_type,
            "severity": a_sev,
            "message": message
        })
        
        # Test deduplication: generate explicit duplicate within 30s
        if random.random() > 0.6:
            dup_time = a_time + timedelta(seconds=random.randint(1, 20))
            alerts.append({
                "timestamp": dup_time,
                "device_id": incident_device,
                "alert_type": a_type,
                "severity": a_sev,
                "message": message
            })

# Pad or slice to get precisely 1000 
if len(alerts) > 1000:
    alerts = alerts[:1000]
else:
    while len(alerts) < 1000:
        a_time = current_time + timedelta(seconds=random.randint(1, 3600))
        current_time = a_time
        alerts.append({
            "timestamp": a_time,
            "device_id": random.choice(devices),
            "alert_type": "Minor Glitch",
            "severity": "Info",
            "message": "Routine background log"
        })

# Sort chronologically
alerts.sort(key=lambda x: x["timestamp"])

with open("data/alerts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp","device_id","alert_type","severity","message"])
    for a in alerts:
        writer.writerow([
            a["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
            a["device_id"],
            a["alert_type"],
            a["severity"],
            a["message"]
        ])

print(f"Generated {len(alerts)} synthetic alerts successfully to data/alerts.csv")
