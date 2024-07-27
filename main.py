from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import os
import mimetypes

from app.controllers.file_processor import save_file

app = FastAPI()

UPLOAD_DIRECTORY = "./uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}

def is_allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        if not is_allowed_file(file.filename):
            raise HTTPException(status_code=400, detail=f"File {file.filename} has an unsupported file type")
        
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
        if os.path.exists(file_path):
            raise HTTPException(status_code=400, detail=f"File {file.filename} already exists")
        
        try:
            save_file(file, file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "Files successfully uploaded"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

