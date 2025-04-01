# app/models/document_model.py
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    userid: str
    docname: str
    description: str
    link: str

class DocumentGet(BaseModel):
    userid: str