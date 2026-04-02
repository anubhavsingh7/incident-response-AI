from pydantic import BaseModel

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
