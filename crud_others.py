from sqlalchemy.orm import Session
from models import Doctor, Appointment, Prescription, LabResult
from schemas import DoctorCreate, AppointmentCreate, PrescriptionCreate, LabResultCreate
from typing import List

# Doctor
def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def create_doctors(db: Session, doctors: List[DoctorCreate]):
    db_doctors = [Doctor(**doctor.model_dump()) for doctor in doctors]
    db.add_all(db_doctors)
    db.commit()
    for doctor in db_doctors:
        db.refresh(doctor)
    return f"{len(doctors)} doctors inserted successfully."

# Appointment
def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = Appointment(**appointment.model_dump())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def create_appointments(db: Session, appointments: List[AppointmentCreate]):
    db_appointments = [Appointment(**appt.model_dump()) for appt in appointments]
    db.add_all(db_appointments)
    db.commit()
    for appt in db_appointments:
        db.refresh(appt)
    return f"{len(appointments)} appointments inserted successfully."


# Prescription
def create_prescription(db: Session, prescription: PrescriptionCreate):
    db_prescription = Prescription(**prescription.model_dump())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription


def create_prescriptions(db: Session, prescriptions: List[PrescriptionCreate]):
    db_prescriptions = [Prescription(**pres.model_dump()) for pres in prescriptions]
    db.add_all(db_prescriptions)
    db.commit()
    for pres in db_prescriptions:
        db.refresh(pres)
    return f"{len(prescriptions)} prescriptions inserted successfully."


# Lab Result
def create_lab_result(db: Session, lab_result: LabResultCreate):
    db_lab_result = LabResult(**lab_result.model_dump())
    db.add(db_lab_result)
    db.commit()
    db.refresh(db_lab_result)
    return db_lab_result

def create_lab_results(db: Session, lab_results: List[LabResultCreate]):
    db_lab_results = [LabResult(**result.model_dump()) for result in lab_results]
    db.add_all(db_lab_results)
    db.commit()
    for result in db_lab_results:
        db.refresh(result)
    return f"{len(lab_results)} lab results inserted successfully."