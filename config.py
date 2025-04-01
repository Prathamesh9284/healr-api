# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FIREBASE_DB_URL = os.getenv('FIREBASE_DB_URL')
    GROQ_KEY = os.getenv('GROQ_KEY')
    FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
    
    @staticmethod
    def get_firebase_creds():
        import json
        creds_dict = json.loads(Config.FIREBASE_CREDENTIALS)
        creds_dict['private_key'] = creds_dict['private_key'].replace("\\n", "\n")
        return creds_dict