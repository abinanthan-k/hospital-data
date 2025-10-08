from pydantic import BaseModel
from datetime import datetime

class VitalBase(BaseModel):
    id: str
    type: str
    value: str
    unit: str
    timestamp: datetime
    recordedBy: str

class VitalCreate(VitalBase):
    patient_id: str

class Vital(VitalBase):
    class Config:
        orm_mode = True
