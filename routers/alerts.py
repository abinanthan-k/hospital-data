from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.alert import Alert as AlertModel
from schemas.alert import AlertCreate, Alert
from typing import List

router = APIRouter(prefix="/alerts", tags=["Alerts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Alert)
def create_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    db_alert = AlertModel(**alert.dict())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@router.get("/", response_model=List[Alert])
def get_alerts(db: Session = Depends(get_db)):
    return db.query(AlertModel).all()
