# app/services/document_service.py
from app.repositories import FirebaseRepository
from app.models.document_model import DocumentCreate, DocumentGet

class DocumentService:
    def __init__(self):
        self.firebase_repo = FirebaseRepository()
    
    def upload_document(self, document: DocumentCreate):
        data = {
            'docname': document.docname,
            'description': document.description,
            'link': document.link
        }
        self.firebase_repo.push_data(f"healerai/docs/{document.userid}", data)
        return {'message': 'Successful'}
    
    def get_documents(self, query: DocumentGet):
        data = self.firebase_repo.get_data(f"healerai/docs/{query.userid}")
        return {'data': data}