from pydantic import BaseModel
from datetime import date

class PrescriptionBase(BaseModel):
    id: str
    medication: str
    dosage: str
    prescribedBy: str
    uploadedBy: str
    date: date
    reason: str
    claimStatus: str

class PrescriptionCreate(PrescriptionBase):
    patient_id: str

class Prescription(PrescriptionBase):
    class Config:
        orm_mode = True
