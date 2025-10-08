from pydantic import BaseModel
from datetime import date

class ScanReportBase(BaseModel):
    id: str
    type: str
    date: date
    uploadedBy: str
    notes: str
    claimStatus: str

class ScanReportCreate(ScanReportBase):
    patient_id: str

class ScanReport(ScanReportBase):
    class Config:
        orm_mode = True
