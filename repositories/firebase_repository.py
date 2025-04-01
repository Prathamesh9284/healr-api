# app/repositories/firebase_repository.py
from firebase_admin import db
from firebase_admin import credentials, initialize_app
from app.config import Config

class FirebaseRepository:
    def __init__(self):
        cred = credentials.Certificate(Config.get_firebase_creds())
        initialize_app(cred, {'databaseURL': Config.FIREBASE_DB_URL})
    
    def set_data(self, path: str, data: dict):
        ref = db.reference(path)
        ref.set(data)
    
    def push_data(self, path: str, data: dict):
        ref = db.reference(path)
        return ref.push(data)
    
    def get_data(self, path: str):
        ref = db.reference(path)
        return ref.get()
    
    def get_filtered_data(self, path: str, filter_key: str, filter_value: str):
        data = self.get_data(path)
        if data:
            return {key: value for key, value in data.items() if value.get(filter_key) == filter_value}
        return {}