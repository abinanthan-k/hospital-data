from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.vital import Vital as VitalModel
from schemas.vital import VitalCreate, Vital
from typing import List

router = APIRouter(prefix="/vitals", tags=["Vitals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Vital)
def create_vital(vital: VitalCreate, db: Session = Depends(get_db)):
    db_vital = VitalModel(**vital.dict())
    db.add(db_vital)
    db.commit()
    db.refresh(db_vital)
    return db_vital

@router.get("/", response_model=List[Vital])
def get_vitals(db: Session = Depends(get_db)):
    return db.query(VitalModel).all()
