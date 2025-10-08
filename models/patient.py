from sqlalchemy import Column, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Patient(Base):
    __tablename__ = "patients"
    global_health_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    bloodType = Column(String)
    status = Column(Enum("active", "pending", "inactive", name="status_enum"))

    insurance_provider_id = Column(String, ForeignKey("insurance_providers.id"))
    insurance_policy_number = Column(String)

    vitals = relationship("Vital", back_populates="patient")
    test_reports = relationship("TestReport", back_populates="patient")
    prescriptions = relationship("Prescription", back_populates="patient")
    scan_reports = relationship("ScanReport", back_populates="patient")
