from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.test_report import TestReport as TestReportModel
from schemas.test_report import TestReportCreate, TestReport
from typing import List

router = APIRouter(prefix="/test-reports", tags=["Test Reports"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TestReport)
def create_test_report(report: TestReportCreate, db: Session = Depends(get_db)):
    db_report = TestReportModel(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@router.get("/", response_model=List[TestReport])
def get_test_reports(db: Session = Depends(get_db)):
    return db.query(TestReportModel).all()
