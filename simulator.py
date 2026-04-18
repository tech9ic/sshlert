import time
import random
import csv
import os
from datetime import datetime

FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "alerts.csv")

# Logical segmentation of devices
ROUTERS = [f"Router-{i}" for i in range(1, 4)]
SWITCHES = [f"Switch-{i}" for i in range(1, 5)]
SERVERS = [f"Server-App{i}" for i in range(1, 4)] + ["Server-DB1"]

def clear_csv():
    with open(FILE_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["device_id", "timestamp", "alert_type", "severity", "message"])

def append_alerts(alerts):
    with open(FILE_PATH, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for a in alerts:
            writer.writerow([a['device'], a['time'], a['type'], a['severity'], a['message']])

def main():
    print("==========================================")
    print(" 📡 STARTING SHHLERT LOGICAL TRAFFIC ENGINE ")
    print("==========================================\n")
    print(f"[*] Wiping old data from: {FILE_PATH}")
    clear_csv()
    
    print("[*] Simulating Smart Logical Network Activity (Generating logs every 3 seconds).")
    print("[*] Press Ctrl+C to stop.\n")
    
    try:
        while True:
            roll = random.random()
            alerts_to_write = []
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Determine which hardware layer we are hitting
            dev_type_roll = random.random()
            
            if roll < 0.2:
                # 20% chance: Hard Crash Incident
                if dev_type_roll < 0.33:
                    # ROUTER CRASH: Routing protocols fail, causing latency
                    device = random.choice(ROUTERS)
                    cause = random.choice([("BGP Down", "Critical"), ("OSPF Down", "Major"), ("Interface Down", "Critical")])
                    alerts_to_write.append({"device": device, "time": now, "type": cause[0], "severity": cause[1], "message": "Peer adjacency failed"})
                    for _ in range(random.randint(2, 4)):
                        symp = random.choice([("High Latency", "Warning"), ("Packet Loss", "Minor")])
                        alerts_to_write.append({"device": device, "time": now, "type": symp[0], "severity": symp[1], "message": "Secondary network degradation"})
                        
                elif dev_type_roll < 0.66:
                    # SWITCH CRASH: Physical uplinks die, causing flapping
                    device = random.choice(SWITCHES)
                    alerts_to_write.append({"device": device, "time": now, "type": "Interface Down", "severity": "Critical", "message": "Uplink trunk disconnected"})
                    for _ in range(random.randint(2, 3)):
                        symp = random.choice([("Port Flapping", "Warning"), ("Packet Loss", "Minor")])
                        alerts_to_write.append({"device": device, "time": now, "type": symp[0], "severity": symp[1], "message": "Link instability detected"})
                        
                else:
                    # SERVER CRASH: Resources exhaust, dropping databases/apps
                    device = random.choice(SERVERS)
                    cause = random.choice([("Disk Space Exhausted", "Critical"), ("CPU High", "Major"), ("Application Crash", "Critical")])
                    alerts_to_write.append({"device": device, "time": now, "type": cause[0], "severity": cause[1], "message": "Hardware boundary breached"})
                    for _ in range(random.randint(2, 4)):
                        symp = random.choice([("Database Disconnect", "Minor"), ("Memory Utilization High", "Warning"), ("High Latency", "Warning")])
                        alerts_to_write.append({"device": device, "time": now, "type": symp[0], "severity": symp[1], "message": "Process starving for resources"})
                
                print(f"[🚨 INCIDENT] {device} underwent '{alerts_to_write[0]['type']}'. Fired {len(alerts_to_write)} total alerts.")
            else:
                # 80% chance: Background Routine Noise mapped properly to hardware
                if dev_type_roll < 0.33:
                    device = random.choice(ROUTERS)
                    alert, sev = random.choice([("High Latency", "Info"), ("Packet Loss", "Info")])
                elif dev_type_roll < 0.66:
                    device = random.choice(SWITCHES)
                    alert, sev = random.choice([("Port Flapping", "Info"), ("License Expiry", "Warning")])
                else:
                    device = random.choice(SERVERS)
                    alert, sev = random.choice([("Memory Utilization High", "Info"), ("CPU High", "Info")])
                
                alerts_to_write.append({"device": device, "time": now, "type": alert, "severity": sev, "message": "Routine telemetry scan"})
                print(f"[〰️ NOISE] {device} logged {alert} ({sev})")
                
            append_alerts(alerts_to_write)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n\n[*] Live Traffic Engine stopped successfully.")

if __name__ == "__main__":
    main()
