from sqlalchemy import Column, String, DateTime, Enum
from db import Base

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(String, primary_key=True)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    type = Column(Enum("info", "warning", "critical", name="alert_type_enum"), nullable=False)
