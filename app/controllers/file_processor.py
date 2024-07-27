def save_file(file, file_path):
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

def process_file(file):
    # Lógica para procesar el archivo
    return {"status": "processed", "filename": file.filename}

