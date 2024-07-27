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
    response = self.client.post("/auth/register", json={"username": "testuser", "password": "testpass"})
    self.assertEqual(response.status_code, 200)

def test_user_login(self):
    response = self.client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    self.assertEqual(response.status_code, 200)

def test_invalid_user_login(self):
    response = self.client.post("/auth/login", json={"username": "wronguser", "password": "wrongpass"})
    self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
