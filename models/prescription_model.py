# app/models/prescription_model.py
from pydantic import BaseModel
from datetime import datetime

class PrescriptionCreate(BaseModel):
    userid: str
    doctor_id: str
    diagnosis_result: str
    medicines: str
    description: str
    date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class PrescriptionGet(BaseModel):
    userid: str
    doctor_id: str