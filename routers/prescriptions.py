from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.prescriptions import Prescription as PrescriptionModel
from schemas.prescription import PrescriptionCreate, Prescription
from typing import List

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Prescription)
def create_prescription(prescription: PrescriptionCreate, db: Session = Depends(get_db)):
    db_prescription = PrescriptionModel(**prescription.dict())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

@router.get("/", response_model=List[Prescription])
def get_prescriptions(db: Session = Depends(get_db)):
    return db.query(PrescriptionModel).all()
