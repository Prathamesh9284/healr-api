# app/routes/document_routes.py
from fastapi import APIRouter, Form
from app.services import DocumentService
from app.models.document_model import DocumentCreate, DocumentGet
from fastapi.responses import JSONResponse

router = APIRouter()
service = DocumentService()

@router.post('/upload_doc')
async def upload_doc(document: DocumentCreate):
    return service.upload_document(document)

@router.post('/get_docs')
async def get_docs(query: DocumentGet):
    return service.get_documents(query)