# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    disease_routes, 
    prescription_routes, 
    message_routes, 
    document_routes, 
    ai_routes
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(disease_routes.router, prefix="/api/disease", tags=["disease"])
app.include_router(prescription_routes.router, prefix="/api/prescription", tags=["prescription"])
app.include_router(message_routes.router, prefix="/api/message", tags=["message"])
app.include_router(document_routes.router, prefix="/api/document", tags=["document"])
app.include_router(ai_routes.router, prefix="/api/ai", tags=["ai"])

@app.get("/")
def root():
    return {"message": "Hello, World!"}