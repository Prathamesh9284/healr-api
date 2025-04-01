# app/routes/prescription_routes.py
from fastapi import APIRouter, Form
from app.services import PrescriptionService
from app.models.prescription_model import PrescriptionCreate, PrescriptionGet
from fastapi.responses import JSONResponse

router = APIRouter()
service = PrescriptionService()

@router.post('/manage_prescription')
async def manage_prescription(prescription: PrescriptionCreate):
    return service.create_prescription(prescription)

@router.post('/get_prescriptions')
async def get_prescriptions(query: PrescriptionGet):
    return service.get_prescriptions(query)