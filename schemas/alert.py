from pydantic import BaseModel
from datetime import datetime

class AlertBase(BaseModel):
    id: str
    message: str
    timestamp: datetime
    type: str

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    class Config:
        orm_mode = True
