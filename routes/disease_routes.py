# app/routes/disease_routes.py
from fastapi import APIRouter, UploadFile, File, Form
from app.services import DiseaseService
from app.models.disease_models import (
    HypertensionInput, DiabetesInput, HeartDiseaseInput,
    BrainTumorInput, SkinDiseaseInput, ChestCancerInput, BreastCancerInput
)
from fastapi.responses import JSONResponse

router = APIRouter()
service = DiseaseService()

@router.post('/hypertension')
async def hypertension(input_data: HypertensionInput):
    return service.predict_hypertension(input_data)

@router.post('/diabetes')
async def diabetes(input_data: DiabetesInput):
    return service.predict_diabetes(input_data)

@router.post('/heartdisease')
async def heartdisease(input_data: HeartDiseaseInput):
    return service.predict_heart_disease(input_data)

@router.post('/braintumor')
async def braintumor(
    image: UploadFile = File(...),
    userid: str = Form(...),
    image_url: str = Form(...)
):
    image_bytes = await image.read()
    input_data = BrainTumorInput(userid=userid, image_url=image_url)
    return service.predict_brain_tumor(image_bytes, input_data)

@router.post('/skindisease')
async def skindisease(
    image: UploadFile = File(...),
    userid: str = Form(...),
    image_url: str = Form(...)
):
    image_bytes = await image.read()
    input_data = SkinDiseaseInput(userid=userid, image_url=image_url)
    return service.predict_skin_disease(image_bytes, input_data)

@router.post('/chestcancer')
async def chestcancer(
    image: UploadFile = File(...),
    userid: str = Form(...),
    image_url: str = Form(...)
):
    image_bytes = await image.read()
    input_data = ChestCancerInput(userid=userid, image_url=image_url)
    return service.predict_chest_cancer(image_bytes, input_data)

@router.post('/breastcancer')
async def breastcancer(
    image: UploadFile = File(...),
    userid: str = Form(...),
    image_url: str = Form(...)
):
    image_bytes = await image.read()
    input_data = BreastCancerInput(userid=userid, image_url=image_url)
    return service.predict_breast_cancer(image_bytes, input_data)

@router.post('/get_disease_probability')
async def get_disease_probability(userid: str = Form(...)):
    return service.get_disease_probability(userid)