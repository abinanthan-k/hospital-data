from pydantic import BaseModel
from datetime import date
from typing import List, Union

class TestReportBase(BaseModel):
    id: str
    name: str
    date: date
    uploadedBy: str
    summary: str
    aiInsights: Union[List[str], str]
    claimStatus: str

class TestReportCreate(TestReportBase):
    patient_id: str

class TestReport(TestReportBase):
    class Config:
        orm_mode = True
