from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Incident:
    incident_id: str
    device: str
    start_time: str
    end_time: str = ""
    alerts_count: int = 0
    severity: str = ""
    root_cause: str = ""
    status: str = "Open"
    duration: str = "0 min"
    alerts: List[Dict] = field(default_factory=list)

    def to_dict(self):
        return {
            "incident_id": self.incident_id,
            "device": self.device,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "alerts_count": self.alerts_count,
            "severity": self.severity,
            "root_cause": self.root_cause,
            "status": self.status,
            "duration": self.duration,
            "alerts": [{"timestamp": a["timestamp_raw"], "message": a["message"], "severity": a["severity"], "type": a["alert_type"]} for a in self.alerts]
        }
