from pydantic import BaseModel
from datetime import datetime

class ReminderBase(BaseModel):
    id: str
    title: str
    due: datetime
    type: str

class ReminderCreate(ReminderBase):
    pass

class Reminder(ReminderBase):
    class Config:
        orm_mode = True
