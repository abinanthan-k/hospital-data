from pydantic import BaseModel

class HospitalBase(BaseModel):
    id: str
    name: str
    email: str
    password: str
    status: str

class HospitalCreate(HospitalBase):
    pass

class Hospital(HospitalBase):
    class Config:
        orm_mode = True
