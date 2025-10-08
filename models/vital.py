from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Vital(Base):
    __tablename__ = "vitals"
    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    value = Column(String, nullable=False)
    unit = Column(String)
    timestamp = Column(DateTime, nullable=False)
    recordedBy = Column(String)

    patient_id = Column(String, ForeignKey("patients.global_health_id"))
    patient = relationship("Patient", back_populates="vitals")
