from sqlalchemy import Column, String, Enum
from db import Base

class InsuranceProvider(Base):
    __tablename__ = "insurance_providers"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    adminUsername = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    status = Column(Enum("active", "pending", "inactive", name="status_enum"), nullable=False)
