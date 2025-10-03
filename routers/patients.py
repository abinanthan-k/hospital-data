from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_patients
import schemas,models
from typing import List, Union, Optional

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/all")
def get_all_patients(db:Session = Depends(get_db)):
    return crud_patients.get_all_patients(db)

@router.get("/")
def get_patient(id: Optional[int] = None, name:Optional[str] = None, 
                age:Optional[int] = None, contact_number:Optional[str] = None,
                address: Optional[str] = None, medical_history: Optional[str] = None,
                db:Session = Depends(get_db)):
    filters = []
    patients = models.Patient
    query = db.query(patients)
    if id:
        filters.append(patients.id == id)
    if name:
        filters.append(patients.name.ilike(f"%{name}%"))
    if age:
        filters.append(patients.age == age)
    if contact_number:
        filters.append(patients.contact_number.ilike(f"%{contact_number}%"))
    if address:
        filters.append(patients.address.ilike(f"%{address}%"))
    if medical_history:
        filters.append(patients.medical_history.ilike(f"%{medical_history}%"))
            
    if filters:
        query = query.filter(*filters)
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No patient(s) found matching the criteria!")
    return results


@router.post("/")
def create_new_patient(patient:Union[schemas.PatientCreate, List[schemas.PatientCreate]], 
                       db:Session = Depends(get_db)):
    if isinstance(patient, list):
        return crud_patients.create_patients(db, patient)
    return crud_patients.create_patient(db, patient)

@router.put("/")
def update_patient(id:int, patient:schemas.PatientUpdate, db:Session = Depends(get_db)):
    new_patient = crud_patients.update_patient(db, id, patient)
    return new_patient