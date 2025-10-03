from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_others
import schemas, models
from typing import List, Optional

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud_others.create_doctor(db, doctor)

@router.get("/search", response_model=List[schemas.Doctor])
def search_doctors(
    id: Optional[int] = None,
    name: Optional[str] = None,
    specialization: Optional[str] = None,
    db: Session = Depends(get_db)
):
    filters = []
    if id:
        filters.append(models.Doctor.id == id)
    if name:
        filters.append(models.Doctor.name.ilike(f"%{name}%"))
    if specialization:
        filters.append(models.Doctor.specialization.ilike(f"%{specialization}%"))

    query = db.query(models.Doctor)
    if filters:
        query = query.filter(*filters)
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No doctor(s) found matching the criteria!")
    return results