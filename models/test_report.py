from sqlalchemy import Column, Enum, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class TestReport(Base):
    __tablename__ = "test_reports"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    uploadedBy = Column(String)
    summary = Column(String)
    aiInsights = Column(String)  # Store as comma-separated or JSON string
    claimStatus = Column(Enum("Approved", "Pending", "Rejected", name="claim_status_enum"))

    patient_id = Column(String, ForeignKey("patients.global_health_id"))
    patient = relationship("Patient", back_populates="test_reports")
