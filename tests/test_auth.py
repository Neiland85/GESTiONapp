import unittest
import requests

class TestAuth(unittest.TestCase):

    def setUp(self):
<<<<<<< HEAD
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
=======
        self.base_url = "http://www.kurtgodelismydad.io

    def test_invalid_user_login(self):
        response = requests.post(f"{self.base_url}/login", data={"username": "invalid", "password": "wrong"})
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        response = requests.post(f"{self.base_url}/login", data={"username": "validuser", "password": "rightpassword"})
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        response = requests.post(f"{self.base_url}/register", data={"username": "newuser", "password": "newpassword"})
        self.assertEqual(response.status_code, 200)
>>>>>>> 4f404e9 (Fix bcrypt attribute error and update test endpoints)

if __name__ == "__main__":
    unittest.main()
