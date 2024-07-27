from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    id: int
    name: str
    content: str
    processed: bool

class ProcessingHistory(BaseModel):
    document_id: int
    filename: str
    status: str
    timestamp: str  # Considera usar datetime

class Notification(BaseModel):
    email: str
    message: str

