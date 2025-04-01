# app/routes/message_routes.py
from fastapi import APIRouter, Form
from app.services import MessageService
from app.models.message_model import MessageCreate, MessageGet
from fastapi.responses import JSONResponse

router = APIRouter()
service = MessageService()

@router.post('/send_message')
async def send_message(message: MessageCreate):
    return service.send_message(message)

@router.post('/get_message')
async def get_message(query: MessageGet):
    return service.get_messages(query)