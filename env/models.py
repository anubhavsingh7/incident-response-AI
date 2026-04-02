from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    incident_id: int
    logs: str
    alert: str

class Action(BaseModel):
    issue_type: str
    severity: str
    resolution: str

class Reward(BaseModel):
    score: float
    feedback: Optional[str] = None