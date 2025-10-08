from sqlalchemy import Column, Enum, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(String, primary_key=True)
    medication = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    prescribedBy = Column(String)
    uploadedBy = Column(String)
    date = Column(Date, nullable=False)
    reason = Column(String)
    claimStatus = Column(Enum("Approved", "Pending", "Rejected", name="claim_status_enum"))

    patient_id = Column(String, ForeignKey("patients.global_health_id"))
    patient = relationship("Patient", back_populates="prescriptions")
