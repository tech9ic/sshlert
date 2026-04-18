import time
import random
import csv
import os
from datetime import datetime

FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "alerts.csv")

# Logical segmentation of devices
ROUTERS = [f"Router-{i}" for i in range(1, 4)]
SWITCHES = [f"Switch-{i}" for i in range(1, 4)]
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
            
            if roll < 0.25:
                # 25% chance: Hard Crash Incident
                if dev_type_roll < 0.33:
                    # ROUTER CRASH: Routing protocols fail, causing latency
                    device = random.choice(ROUTERS)
                    cause = random.choice([("BGP Down", "Critical", "%BGP-5-ADJCHANGE: neighbor x.x.x.x Down - BGP Notification sent"), ("OSPF Down", "Major", "%OSPF-5-ADJCHG: Process 1, Nbr x.x.x.x on GigabitEthernet0/1 from FULL to DOWN"), ("Interface Down", "Critical", "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down")])
                    alerts_to_write.append({"device": device, "time": now, "type": cause[0], "severity": cause[1], "message": cause[2]})
                    for _ in range(random.randint(3, 5)):
                        symp = random.choice([("High Latency", "Warning", "ICMP response > 500ms"), ("Packet Loss", "Minor", "SNMP Drop Counter Incrementing")])
                        alerts_to_write.append({"device": device, "time": now, "type": symp[0], "severity": symp[1], "message": symp[2]})
                        
                elif dev_type_roll < 0.66:
                    # SWITCH CRASH: Physical uplinks die, causing flapping
                    device = random.choice(SWITCHES)
                    alerts_to_write.append({"device": device, "time": now, "type": "Interface Down", "severity": "Critical", "message": "%PHY-4-DOWN: Port 1/0/24 link state down"})
                    for _ in range(random.randint(2, 4)):
                        symp = random.choice([("Port Flapping", "Warning", "%ETHPORT-5-IF_DOWN_LINK_FAILURE"), ("Packet Loss", "Minor", "FCS Errors increasing")])
                        alerts_to_write.append({"device": device, "time": now, "type": symp[0], "severity": symp[1], "message": symp[2]})
                        
                else:
                    # SERVER CRASH: Resources exhaust, dropping databases/apps
                    device = random.choice(SERVERS)
                    cause = random.choice([("Disk Space Exhausted", "Critical", "syslog: /var/log filesystem is 99% full"), ("CPU High", "Major", "syslog: load average 15.42"), ("Application Crash", "Critical", "kernel: [1234.567] java(1234): segfault at 0 ip 000 sp 000 error 4")])
                    alerts_to_write.append({"device": device, "time": now, "type": cause[0], "severity": cause[1], "message": cause[2]})
                    for _ in range(random.randint(2, 5)):
                        symp = random.choice([("Database Disconnect", "Minor", "psycopg2.OperationalError: connection refused"), ("Memory Utilization High", "Warning", "OOM-killer invoked"), ("High Latency", "Warning", "API response > 2000ms")])
                        alerts_to_write.append({"device": device, "time": now, "type": symp[0], "severity": symp[1], "message": symp[2]})
                
                print(f"[🚨 INCIDENT] {device} underwent '{alerts_to_write[0]['type']}'. Fired {len(alerts_to_write)} total alerts within 1 sec.")
            else:
                # 75% chance: Dialect Background Noise
                if dev_type_roll < 0.33:
                    device = random.choice(ROUTERS)
                    alert, sev, msg = random.choice([("High Latency", "Info", "ICMP jitter detected"), ("Packet Loss", "Info", "Random trailing drops"), ("Admin Login", "Info", "%SEC_LOGIN-5-LOGIN_SUCCESS")])
                elif dev_type_roll < 0.66:
                    device = random.choice(SWITCHES)
                    alert, sev, msg = random.choice([("Port Flapping", "Info", "%SPANTREE-5-TOPOTRAP"), ("License Expiry", "Warning", "Feature license warning: 30 days remaining"), ("Config Change", "Info", "%SYS-5-CONFIG_I: Configured from console by admin")])
                else:
                    device = random.choice(SERVERS)
                    alert, sev, msg = random.choice([("Memory Utilization High", "Info", "Cache flushing routine"), ("CPU High", "Info", "Cronjob execution block"), ("Admin Login", "Info", "sshd: session opened for user root")])
                
                alerts_to_write.append({"device": device, "time": now, "type": alert, "severity": sev, "message": msg})
                print(f"[〰️ NOISE] {device} logged {alert} ({sev})")
                
            append_alerts(alerts_to_write)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n\n[*] Live Traffic Engine stopped successfully.")

if __name__ == "__main__":
    main()
