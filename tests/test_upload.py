import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestFileUpload(unittest.TestCase):
    def test_upload_jpg(self):
        with open("tests/test_files/test.jpg", "rb") as file:
            response = client.post("/upload/", files={"files": file})
            self.assertEqual(response.status_code, 200)

    def test_upload_pdf(self):
        with open("tests/test_files/test.pdf", "rb") as file:
            response = client.post("/upload/", files={"files": file})
            self.assertEqual(response.status_code, 200)

    def test_upload_png(self):
        with open("tests/test_files/test.png", "rb") as file:
            response = client.post("/upload/", files={"files": file})
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
