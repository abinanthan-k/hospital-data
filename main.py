from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import schemas, models
import crud_patients
from typing import List, Union, Optional
from routers import patients, labreports, appointments, prescriptions, doctors

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(prescriptions.router)
app.include_router(labreports.router)
app.include_router(doctors.router)



@app.get("/")
def root():
    return {"Status": "Healthy"}
    
    
    
