from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.reminder import Reminder as ReminderModel
from schemas.reminder import ReminderCreate, Reminder
from typing import List

router = APIRouter(prefix="/reminders", tags=["Reminders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Reminder)
def create_reminder(reminder: ReminderCreate, db: Session = Depends(get_db)):
    db_reminder = ReminderModel(**reminder.dict())
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

@router.get("/", response_model=List[Reminder])
def get_reminders(db: Session = Depends(get_db)):
    return db.query(ReminderModel).all()
