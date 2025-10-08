from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models.insurance import InsuranceProvider as InsuranceModel
from schemas.insurance import InsuranceProviderCreate, InsuranceProvider
from typing import List

router = APIRouter(prefix="/insurance", tags=["Insurance Providers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=InsuranceProvider)
def create_insurance(insurance: InsuranceProviderCreate, db: Session = Depends(get_db)):
    db_insurance = InsuranceModel(**insurance.dict())
    db.add(db_insurance)
    db.commit()
    db.refresh(db_insurance)
    return db_insurance

@router.get("/", response_model=List[InsuranceProvider])
def get_insurance_providers(db: Session = Depends(get_db)):
    return db.query(InsuranceModel).all()
