from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Patient
class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    contact_number: str
    address: str
    medical_history: Optional[str] = None

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    contact_number: Optional[str] = None
    address: Optional[str] = None
    medical_history: Optional[str] = None

class Patient(PatientCreate):
    id: int
    class Config:
        orm_mode = True

# Doctor
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    contact_number: str

class Doctor(DoctorCreate):
    id: int
    class Config:
        orm_mode = True

# Appointment
class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime
    reason: Optional[str] = None

class Appointment(AppointmentCreate):
    id: int
    class Config:
        orm_mode = True

# Prescription
class PrescriptionCreate(BaseModel):
    patient_id: int
    doctor_id: int
    medication: str
    dosage: str
    instructions: Optional[str] = None

class Prescription(PrescriptionCreate):
    id: int
    class Config:
        orm_mode = True

# Lab Result
class LabResultCreate(BaseModel):
    patient_id: int
    test_name: str
    result: str
    date: datetime

class LabResult(LabResultCreate):
    id: int
    class Config:
        orm_mode = True
