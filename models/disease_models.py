# app/models/disease_models.py
from pydantic import BaseModel
from typing import Optional

class DiseasePredictionInput(BaseModel):
    gender: str
    age: str
    userid: str

class HypertensionInput(DiseasePredictionInput):
    cigsPerDay: str
    BPMeds: str
    totChol: str
    sysBP: str
    diaBP: str
    weight: str
    height: str
    heartRate: str
    glucose: str

class DiabetesInput(DiseasePredictionInput):
    hyperTension: str
    heartDisease: str
    cigsPerDay: str
    weight: str
    height: str
    hba1c: str
    glucose: str

class HeartDiseaseInput(DiseasePredictionInput):
    cigsPerDay: str
    cholesterol: str
    weight: str
    height: str
    glucose: str
    ap_lo: str
    ap_hi: str
    alco: str
    active: str

class ImagePredictionInput(BaseModel):
    userid: str
    image_url: str

class BrainTumorInput(ImagePredictionInput):
    pass

class SkinDiseaseInput(ImagePredictionInput):
    pass

class ChestCancerInput(ImagePredictionInput):
    pass

class BreastCancerInput(ImagePredictionInput):
    pass