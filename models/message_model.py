# app/models/message_model.py
from pydantic import BaseModel

class MessageCreate(BaseModel):
    userid: str
    message: str
    community: str
    timestamp: str
    userImageURL: str

class MessageGet(BaseModel):
    community: str