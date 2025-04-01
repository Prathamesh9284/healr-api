# app/services/ai_service.py
from langchain_groq import ChatGroq
from app.config import Config

class AIService:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.2-90b-vision-preview",
            temperature=0,
            groq_api_key=Config.GROQ_KEY
        )
    
    def get_llama_response(self, query: str, prompt: str):
        response = self.llm.invoke([query, prompt])
        return response.content