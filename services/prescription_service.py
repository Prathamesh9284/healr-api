# app/services/prescription_service.py
from app.repositories import FirebaseRepository
from app.models.prescription_model import PrescriptionCreate, PrescriptionGet

class PrescriptionService:
    def __init__(self):
        self.firebase_repo = FirebaseRepository()
    
    def create_prescription(self, prescription: PrescriptionCreate):
        data = {
            'userid': prescription.userid,
            'doctor_id': prescription.doctor_id,
            'diagnosis_result': prescription.diagnosis_result,
            'date': prescription.date,
            'prescriptionid': f"RX{int(prescription.date.timestamp())}{prescription.userid}",
            'medicines': prescription.medicines,
            'description': prescription.description
        }
        
        self.firebase_repo.push_data(f"prescriptions/{prescription.userid}", data)
        return {'message': 'Successful'}
    
    def get_prescriptions(self, query: PrescriptionGet):
        data = self.firebase_repo.get_filtered_data(
            f"prescriptions/{query.userid}",
            'doctor_id',
            query.doctor_id
        )
        return {'data': data}