from sqlalchemy import Column, Enum, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class ScanReport(Base):
    __tablename__ = "scan_reports"
    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    uploadedBy = Column(String)
    notes = Column(String)
    claimStatus = Column(Enum("Approved", "Pending", "Rejected", name="claim_status_enum"))

    patient_id = Column(String, ForeignKey("patients.global_health_id"))
    patient = relationship("Patient", back_populates="scan_reports")
