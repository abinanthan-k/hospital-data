from sqlalchemy import Column, String, Enum
from db import Base

class Hospital(Base):
    __tablename__ = "hospitals"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    status = Column(Enum("active", "pending", "inactive", name="status_enum"), nullable=False)
