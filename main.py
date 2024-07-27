from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import os

from app.file_processor import save_file  # Asumiendo que tienes esta función

app = FastAPI()

UPLOAD_DIRECTORY = "./uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
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

