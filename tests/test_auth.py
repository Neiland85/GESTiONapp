import unittest
from fastapi.testclient import TestClient
from app.main import create_app

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(create_app())

    def test_user_registration(self):
        response = self.app.post("/auth/register/", json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.app.post("/auth/token", data={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_login(self):
        response = self.app.post("/auth/token", data={"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
