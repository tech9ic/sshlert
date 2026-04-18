# configuration parameters
CORRELATION_WINDOW_MINUTES = 5

ALERT_CATEGORIES = {
    "Interface Down": "Network",
    "Packet Loss": "Network",
    "High Latency": "Network",
    "Port Flapping": "Network",
    "BGP Down": "Routing",
    "OSPF Down": "Routing",
    "CPU High": "System",
    "Memory Utilization High": "System",
    "Disk Space Exhausted": "System",
    "License Expiry": "System",
    "Application Crash": "Application",
    "Database Disconnect": "Application"
}

SEVERITY_LEVELS = {
    "Critical": 4,
    "Major": 3,
    "Minor": 2,
    "Warning": 1,
    "Info": 0
}

ROOT_CAUSE_WEIGHTS = {
    "Interface Down": 100,
    "Disk Space Exhausted": 90,
    "CPU High": 80,
    "Memory Utilization High": 80,
    "Application Crash": 70,
    "OSPF Down": 60,
    "BGP Down": 60,
    "Database Disconnect": 50,
    "Packet Loss": 40,
    "Port Flapping": 30,
    "High Latency": 20,
    "License Expiry": 10
}
