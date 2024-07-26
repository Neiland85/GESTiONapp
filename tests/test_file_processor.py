# tests/test_file_processor.py
import unittest
from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

class TestFileUpload(unittest.TestCase):
    def test_upload_files(self):
        # Ruta del archivo de prueba
        test_file_path = os.path.join(os.path.dirname(__file__), "test_file.pdf")
        
        # Asegurarse de que el archivo existe
        self.assertTrue(os.path.exists(test_file_path), "Test file does not exist")

        # Abrir el archivo de prueba y realizar la solicitud
        with open(test_file_path, "rb") as file:
            response = client.post("/upload/", files={"files": file})
        
        # Verificar la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertIn("Files successfully uploaded", response.json()["message"])

if __name__ == '__main__':
    unittest.main()

