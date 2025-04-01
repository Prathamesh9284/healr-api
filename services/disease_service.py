# app/services/disease_service.py
from app.repositories import PredictionRepository, FirebaseRepository
from app.models.disease_models import (
    HypertensionInput, DiabetesInput, HeartDiseaseInput,
    BrainTumorInput, SkinDiseaseInput, ChestCancerInput, BreastCancerInput
)

class DiseaseService:
    def __init__(self):
        self.prediction_repo = PredictionRepository()
        self.firebase_repo = FirebaseRepository()
    
    def predict_hypertension(self, input_data: HypertensionInput):
        data = {
            'male': int(input_data.gender),
            'age': int(input_data.age),
            'cigsPerDay': int(input_data.cigsPerDay),
            'BPMeds': int(input_data.BPMeds),
            'totChol': int(input_data.totChol),
            'sysBP': int(input_data.sysBP),
            'diaBP': int(input_data.diaBP),
            'BMI': int(input_data.weight) / ((int(input_data.height)/ 100) ** 2),
            'heartRate': int(input_data.heartRate),
            'glucose': int(input_data.glucose),
        }
        
        prediction = self.prediction_repo.predict_structured('hypertensionfull', data)
        
        result = data.copy()
        result['probability'] = float(prediction[1])
        
        self.firebase_repo.set_data(
            f"diseaseProbability/{input_data.userid}/hypertension",
            result
        )
        
        return {'status': 'success'}
    
    def predict_diabetes(self, input_data: DiabetesInput):
        data = {
            'gender': input_data.gender,
            'age': input_data.age,
            'hypertension': input_data.hyperTension,
            'heart_disease': input_data.heartDisease,
            'smoking_history': 1 if int(input_data.cigsPerDay) > 0 else 0,
            'bmi': int(input_data.weight) / ((int(input_data.height) / 100) ** 2),
            'HbA1c_level': input_data.hba1c,
            'blood_glucose_level': input_data.glucose
        }
        
        prediction = self.prediction_repo.predict_structured('diabetesfull', data)
        
        result = {'heartdisease': float(prediction[1])}
        
        self.firebase_repo.push_data("diseaseProbability/", result)
        
        return {'status': 'success'}
    
    def predict_heart_disease(self, input_data: HeartDiseaseInput):
        data = {
            'age': int(input_data.age)*365, 
            'gender': int(input_data.gender),
            'height': int(input_data.height),
            'weight': int(input_data.weight),
            'ap_hi': int(input_data.ap_hi),
            'ap_lo': int(input_data.ap_lo),
            'cholesterol': int(input_data.cholesterol),
            'gluc': int(input_data.glucose),
            'smoke': 1 if int(input_data.cigsPerDay) > 0 else 0,
            'alco': int(input_data.alco),
            'active': int(input_data.active),
            'bmi': int(input_data.weight) / ((int(input_data.height) / 100) ** 2)
        }
        
        prediction = self.prediction_repo.predict_structured('heartfull', data)
        
        result = data.copy()
        result['probability'] = float(prediction[1])
        
        self.firebase_repo.set_data(
            f"diseaseProbability/{input_data.userid}/heartDisease",
            result
        )
        
        return {'status': 'success'}
    
    def predict_brain_tumor(self, image_bytes: bytes, input_data: BrainTumorInput):
        prediction = self.prediction_repo.predict_image('brainTumor', image_bytes)
        
        result = {
            'probability': prediction['probability'],
            'predicted_class': prediction['predicted_class'],
            'image_url': input_data.image_url
        }
        
        self.firebase_repo.set_data(
            f"diseaseProbability/{input_data.userid}/brainTumor",
            result
        )
        
        return {'status': 'success'}
    
    def predict_skin_disease(self, image_bytes: bytes, input_data: SkinDiseaseInput):
        prediction = self.prediction_repo.predict_image('skin', image_bytes)
        
        result = {
            'probability': prediction['probability'],
            'predicted_class': prediction['predicted_class'],
            'image_url': input_data.image_url
        }
        
        self.firebase_repo.set_data(
            f"diseaseProbability/{input_data.userid}/skindisease",
            result
        )
        
        return {'status': 'success'}
    
    def predict_chest_cancer(self, image_bytes: bytes, input_data: ChestCancerInput):
        prediction = self.prediction_repo.predict_image('chestCancer', image_bytes)
        
        result = {
            'probability': prediction['probability'],
            'predicted_class': prediction['predicted_class'],
            'image_url': input_data.image_url
        }
        
        self.firebase_repo.set_data(
            f"diseaseProbability/{input_data.userid}/chestcancer",
            result
        )
        
        return {'status': 'success'}
    
    def predict_breast_cancer(self, image_bytes: bytes, input_data: BreastCancerInput):
        prediction = self.prediction_repo.predict_image('breastCancer', image_bytes)
        
        result = {
            'probability': prediction['probability'],
            'predicted_class': prediction['predicted_class'],
            'image_url': input_data.image_url
        }
        
        self.firebase_repo.set_data(
            f"diseaseProbability/{input_data.userid}/breastcancer",
            result
        )
        
        return {'status': 'success'}
    
    def get_disease_probability(self, userid: str):
        data = self.firebase_repo.get_data(f"diseaseProbability/{userid}")
        return {'data': data}