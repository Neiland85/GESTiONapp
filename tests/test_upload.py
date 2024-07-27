import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestUpload(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_upload_file(self):
        with open("testfile.txt", "wb") as f:
            f.write(b"this is a test file")

        with open("testfile.txt", "rb") as f:
            response = self.client.post("/upload", files={"file": f})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("filename", response.json())

if __name__ == '__main__':
    unittest.main()
