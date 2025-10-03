from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_others
import schemas, models
from typing import List, Optional

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud_others.create_appointment(db, appointment)

@router.get("/search", response_model=List[schemas.Appointment])
def search_appointments(
    id: Optional[int] = None,
    patient_id: Optional[int] = None,
    doctor_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    filters = []
    if id:
        filters.append(models.Appointment.id == id)
    if patient_id:
        filters.append(models.Appointment.patient_id == patient_id)
    if doctor_id:
        filters.append(models.Appointment.doctor_id == doctor_id)

    query = db.query(models.Appointment)
    if filters:
        query = query.filter(*filters)
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No appointment(s) found matching the criteria!")
    return results