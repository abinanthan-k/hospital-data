from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models.patient import Patient as PatientModel
from schemas.patient import PatientCreate, Patient
from typing import List

router = APIRouter(prefix="/patients", tags=["Patients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = PatientModel(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=List[Patient])
def get_patients(db: Session = Depends(get_db)):
    return db.query(PatientModel).all()

@router.get("/{ghid}", response_model=Patient)
def get_patient(ghid: str, db: Session = Depends(get_db)):
    patient = db.query(PatientModel).filter(PatientModel.global_health_id == ghid).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
