# app/routes/__init__.py
from .disease_routes import router as disease_router
from .prescription_routes import router as prescription_router
from .message_routes import router as message_router
from .document_routes import router as document_router
from .ai_routes import router as ai_router