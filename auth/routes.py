from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from auth.utils import verify_password, get_password_hash, create_access_token
from models.patient import Patient
from models.hospital import Hospital
from models.insurance import InsuranceProvider
from schemas.patient import PatientCreate
from schemas.hospital import HospitalCreate
from schemas.insurance import InsuranceProviderCreate
from db import SessionLocal
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    role = form_data.scopes[0] if form_data.scopes else None
    user = None

    if role == "patient":
        user = db.query(Patient).filter(Patient.globalHealthId == form_data.username).first()
    elif role == "hospital":
        user = db.query(Hospital).filter(Hospital.email == form_data.username).first()
    elif role == "insurance":
        user = db.query(InsuranceProvider).filter(InsuranceProvider.adminUsername == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": form_data.username, "role": role}, expires_delta=timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}

@router.post("/signup/patient")
def signup_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(patient.password)
    db_patient = Patient(**patient.dict(), password=hashed_password)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return {"message": "Patient registered successfully"}

@router.post("/signup/hospital")
def signup_hospital(hospital: HospitalCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(hospital.password)
    db_hospital = Hospital(**hospital.dict(), password=hashed_password)
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return {"message": "Hospital registered successfully"}

@router.post("/signup/insurance")
def signup_insurance(insurance: InsuranceProviderCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(insurance.password)
    db_insurance = InsuranceProvider(**insurance.dict(), password=hashed_password)
    db.add(db_insurance)
    db.commit()
    db.refresh(db_insurance)
    return {"message": "Insurance provider registered successfully"}
