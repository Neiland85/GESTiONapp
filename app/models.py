# app/models.py

from pydantic import BaseModel

class Document(BaseModel):
    id: int
    name: str
    content: str
    processed: bool

