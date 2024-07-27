import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_user_registration(self):
        response = self.client.post("/auth/register/", json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.client.post("/auth/token", data={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_login(self):
        response = self.client.post("/auth/token", data={"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
