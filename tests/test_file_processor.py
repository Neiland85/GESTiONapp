# tests/test_file_processor.py
import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestFileUpload(unittest.TestCase):
    def test_upload_files(self):
        with open("test_file.pdf", "rb") as file:
            response = client.post("/upload/", files={"files": file})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Files successfully uploaded", response.json()["message"])

if __name__ == '__main__':
    unittest.main()

