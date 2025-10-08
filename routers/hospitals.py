from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models.hospital import Hospital as HospitalModel
from schemas.hospital import HospitalCreate, Hospital
from typing import List

router = APIRouter(prefix="/hospitals", tags=["Hospitals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Hospital)
def create_hospital(hospital: HospitalCreate, db: Session = Depends(get_db)):
    db_hospital = HospitalModel(**hospital.dict())
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital

@router.get("/", response_model=List[Hospital])
def get_hospitals(db: Session = Depends(get_db)):
    return db.query(HospitalModel).all()
