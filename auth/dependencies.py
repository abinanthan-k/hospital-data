from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from auth.utils import SECRET_KEY, ALGORITHM
from db import SessionLocal
from models.patient import Patient
from models.hospital import Hospital
from models.insurance import InsuranceProvider

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Invalid credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role = payload.get("role")
        user_id = payload.get("sub")
    except JWTError:
        raise credentials_exception

    if role == "patient":
        user = db.query(Patient).filter(Patient.globalHealthId == user_id).first()
    elif role == "hospital":
        user = db.query(Hospital).filter(Hospital.email == user_id).first()
    elif role == "insurance":
        user = db.query(InsuranceProvider).filter(InsuranceProvider.adminUsername == user_id).first()
    else:
        raise credentials_exception

    if not user:
        raise credentials_exception
    return user
