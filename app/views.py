# app/views.py

from fastapi import APIRouter, Depends
from app.models import Document

router = APIRouter()

@router.get("/documents/{document_id}")
async def get_document(document_id: int):
    # Aquí puedes añadir lógica para obtener un documento por ID
    return {"document_id": document_id, "name": "Example Document", "content": "This is an example document.", "processed": False}

@router.post("/documents/")
async def create_document(document: Document):
    # Aquí puedes añadir lógica para crear un nuevo documento
    return {"message": "Document created successfully", "document": document}

