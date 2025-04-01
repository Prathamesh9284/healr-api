# app/repositories/prediction_repository.py
import joblib
import tensorflow as tf
import pandas as pd
import numpy as np
from PIL import Image
import io

class PredictionRepository:
    def __init__(self):
        self.models = {
            'diabetesfull': joblib.load('models/diabetesfull.pkl'),
            'diabeteshalf': joblib.load('models/diabeteshalf.pkl'),
            'hypertensionfull': joblib.load('models/hypertensionfull.pkl'),
            'hypertensionhalf': joblib.load('models/hypertensionhalf.pkl'),
            'hearthalf': joblib.load('models/hearthalf.pkl'),
            'heartfull': joblib.load('models/heartfull.pkl'),
            'brainTumor': tf.keras.models.load_model('models/tumor.h5'),
            'skin': tf.keras.models.load_model('models/Skin.h5'),
            'chestCancer': tf.keras.models.load_model('models/ChestCancer.h5'),
            'breastCancer': tf.keras.models.load_model('models/BreastCancer.h5')
        }
        
        self.class_names = {
            'brainTumor': {0:'Glioma', 1:'Healthy', 2:'Meningioma', 3:'Pituitary'},
            'chestCancer': {0:'Adenocarcinoma', 1:'Lrge cell Carcinoma', 2:'Normal', 3:'Squamous Cell Carcinoma'},
            'breastCancer': {0:'Normal', 1:'Breast Cancer'},
            'skin': {0: 'Cellulitis', 1: 'Impetigo', 2: 'Athletes Foot', 3: 'Nail Fungus', 
                     4: 'Ringworm', 5: 'Cutaneous Larva Migrans', 6: 'Chickenpox',
                     7:'Measles',8:'Monkeypox' ,9:'Shingles'}
        }
    
    def predict_structured(self, model_name: str, input_data: dict):
        df = pd.DataFrame([input_data])
        model = self.models[model_name]
        if hasattr(model, 'predict_proba'):
            return model.predict_proba(df)[0]
        return model.predict(df)
    
    def predict_image(self, model_name: str, image_bytes: bytes):
        image = Image.open(io.BytesIO(image_bytes))
        resized_image = image.resize((256, 256))
        img_array = np.array(resized_image)
        img_array = np.expand_dims(img_array, axis=0)
        prediction = self.models[model_name].predict(img_array)
        top_class_index = np.argmax(prediction)
        return {
            'predicted_class': self.class_names[model_name][top_class_index],
            'probability': float(prediction[0, top_class_index])
        }