from sqlalchemy.orm import Session
from models import Patient
import schemas
from typing import List
from schemas import DoctorCreate, PatientCreate, AppointmentCreate, PrescriptionCreate, LabResultCreate

# Patients
def create_patient(db:Session, patient:PatientCreate):
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return f"Patient {db_patient.name} has been created successfully."

def create_patients(db:Session, patients:List[PatientCreate]):
    db_patients = [Patient(**patient.model_dump()) for patient in patients]
    db.add_all(db_patients)
    db.commit()
    for patient in db_patients:
        db.refresh(patient)
    return f"{len(patients)} patients has been created and inserted successfully."

def get_patient(db:Session, id:int):
    res = db.query(Patient).filter(Patient.id == id).first()
    if not res:
        return "No Patient with the specified id"
    return res

def update_patient(db:Session, id:int, patient):
    db_patient = get_patient(db, id)
    for key,value in vars(patient).items():
        if not key.startswith("__") and value is not None and db_patient:
            setattr(db_patient, key, value)
    return db_patient

def get_all_patients(db:Session):
    return db.query(Patient).all()


