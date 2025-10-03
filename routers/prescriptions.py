from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_others
import schemas, models
from typing import List, Optional

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])

@router.post("/", response_model=schemas.Prescription)
def create_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    return crud_others.create_prescription(db, prescription)

@router.get("/search", response_model=List[schemas.Prescription])
def search_prescriptions(
    id: Optional[int] = None,
    patient_id: Optional[int] = None,
    doctor_id: Optional[int] = None,
    medication: Optional[str] = None,
    db: Session = Depends(get_db)
):
    filters = []
    if id:
        filters.append(models.Prescription.id == id)
    if patient_id:
        filters.append(models.Prescription.patient_id == patient_id)
    if doctor_id:
        filters.append(models.Prescription.doctor_id == doctor_id)
    if medication:
        filters.append(models.Prescription.medication.ilike(f"%{medication}%"))

    query = db.query(models.Prescription)
    if filters:
        query = query.filter(*filters)
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No prescription(s) found matching the criteria!")
    return results