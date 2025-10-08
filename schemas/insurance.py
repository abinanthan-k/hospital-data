from pydantic import BaseModel

class InsuranceProviderBase(BaseModel):
    id: str
    name: str
    adminUsername: str
    password: str
    status: str

class InsuranceProviderCreate(InsuranceProviderBase):
    pass

class InsuranceProvider(InsuranceProviderBase):
    class Config:
        orm_mode = True
