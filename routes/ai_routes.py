# app/routes/ai_routes.py
from fastapi import APIRouter, Form
from app.services import AIService
from fastapi.responses import JSONResponse

router = APIRouter()
service = AIService()

@router.post("/ai_agent")
async def ai_agent(query: str = Form(...), prompt: str = Form(...)):
    answer = service.get_llama_response(query, prompt)
    return JSONResponse(content={"answer": answer})