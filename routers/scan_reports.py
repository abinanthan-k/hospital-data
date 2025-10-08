from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.scan_report import ScanReport as ScanReportModel
from schemas.scan_report import ScanReportCreate, ScanReport
from typing import List

router = APIRouter(prefix="/scan-reports", tags=["Scan Reports"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ScanReport)
def create_scan_report(report: ScanReportCreate, db: Session = Depends(get_db)):
    db_report = ScanReportModel(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@router.get("/", response_model=List[ScanReport])
def get_scan_reports(db: Session = Depends(get_db)):
    return db.query(ScanReportModel).all()
