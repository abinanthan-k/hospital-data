from sqlalchemy import Column, String, DateTime, Enum
from db import Base

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    due = Column(DateTime, nullable=False)
    type = Column(Enum("medication", "appointment", "general", name="reminder_type_enum"), nullable=False)
