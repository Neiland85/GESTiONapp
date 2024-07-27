import unittest
from fastapi.testclient import TestClient
from main import app
from app.db import fake_users_db, get_password_hash

client = TestClient(app)

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.test_user = {
            "username": "testuser",
            "password": "testpassword"
        }
        self.test_admin = {
            "username": "testadmin",
            "password": "testpassword",
            "role": "admin"
        }
        hashed_password = get_password_hash(self.test_user["password"])
        fake_users_db[self.test_user["username"]] = {
            "username": self.test_user["username"],
            "hashed_password": hashed_password,
            "role": "user"
        }

    def test_user_registration(self):
        response = client.post("/register/", json=self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], self.test_user["username"])

    def test_user_login(self):
        response = client.post("/token", data={"username": self.test_user["username"], "password": self.test_user["password"]})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    def test_invalid_user_login(self):
        response = client.post("/token", data={"username": self.test_user["username"], "password": "wrongpassword"})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
