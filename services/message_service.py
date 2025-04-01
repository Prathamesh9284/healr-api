# app/services/message_service.py
from app.repositories import FirebaseRepository
from app.models.message_model import MessageCreate, MessageGet

class MessageService:
    def __init__(self):
        self.firebase_repo = FirebaseRepository()
    
    def send_message(self, message: MessageCreate):
        message_body = {
            'userid': message.userid,
            'message': message.message,
            'timestamp': message.timestamp,
            'userImageURL': message.userImageURL
        }
        self.firebase_repo.push_data(f"community/{message.community}", message_body)
        return {'message': 'Successful'}
    
    def get_messages(self, query: MessageGet):
        data = self.firebase_repo.get_data(f"community/{query.community}")
        return {'data': data}