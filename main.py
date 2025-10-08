from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine
from routers import (
    patients, hospitals, insurance,
    reminders, alerts, vitals,
    test_reports, prescriptions, scan_reports
)
from auth import routes as auth_routes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Health API", version="1.0")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router)
app.include_router(patients.router)
app.include_router(hospitals.router)
app.include_router(insurance.router)
app.include_router(reminders.router)
app.include_router(alerts.router)
app.include_router(vitals.router)
app.include_router(test_reports.router)
app.include_router(prescriptions.router)
app.include_router(scan_reports.router)


