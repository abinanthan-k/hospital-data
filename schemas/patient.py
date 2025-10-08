from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from schemas.vital import Vital
from schemas.test_report import TestReport
from schemas.prescription import Prescription
from schemas.scan_report import ScanReport

class PatientBase(BaseModel):
    global_health_id: str
    name: str
    password: str
    dob: date
    bloodType: str
    status: str
    insurance_provider_id: Optional[str]
    insurance_policy_number: Optional[str]

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    vitals: List[Vital] = []
    test_reports: List[TestReport] = []
    prescriptions: List[Prescription] = []
    scan_reports: List[ScanReport] = []

    class Config:
        orm_mode = True
