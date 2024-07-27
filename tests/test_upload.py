import unittest
from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

class TestFileUpload(unittest.TestCase):

    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), 'test_files')

    def test_upload_pdf(self):
        with open(os.path.join(self.test_files_dir, "test.pdf"), "rb") as file:
            response = client.post("/upload/", files={"files": ("test.pdf", file, "application/pdf")})
            self.assertEqual(response.status_code, 200)
            self.assertIn("Files successfully uploaded", response.json()["message"])

    def test_upload_jpg(self):
        with open(os.path.join(self.test_files_dir, "test.jpg"), "rb") as file:
            response = client.post("/upload/", files={"files": ("test.jpg", file, "image/jpeg")})
            self.assertEqual(response.status_code, 200)
            self.assertIn("Files successfully uploaded", response.json()["message"])

    def test_upload_png(self):
        with open(os.path.join(self.test_files_dir, "test.png"), "rb") as file:
            response = client.post("/upload/", files={"files": ("test.png", file, "image/png")})
            self.assertEqual(response.status_code, 200)
            self.assertIn("Files successfully uploaded", response.json()["message"])

    def test_upload_invalid_file_type(self):
        with open(os.path.join(self.test_files_dir, "test.txt"), "rb") as file:
            response = client.post("/upload/", files={"files": ("test.txt", file, "text/plain")})
            self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()

