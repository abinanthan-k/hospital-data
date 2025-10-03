from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_others
import schemas, models
from typing import List, Optional

router = APIRouter(prefix="/lab-results", tags=["Lab Results"])

@router.post("/", response_model=schemas.LabResult)
def create_lab_result(lab_result: schemas.LabResultCreate, db: Session = Depends(get_db)):
    return crud_others.create_lab_result(db, lab_result)

@router.get("/search", response_model=List[schemas.LabResult])
def search_lab_results(
    id: Optional[int] = None,
    patient_id: Optional[int] = None,
    test_name: Optional[str] = None,
    db: Session = Depends(get_db)
):
    filters = []
    if id:
        filters.append(models.LabResult.id == id)
    if patient_id:
        filters.append(models.LabResult.patient_id == patient_id)
    if test_name:
        filters.append(models.LabResult.test_name.ilike(f"%{test_name}%"))

    query = db.query(models.LabResult)
    if filters:
        query = query.filter(*filters)
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No lab result(s) found matching the criteria!")
    return results