import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_item_not_found(self):
        response = self.client.get("/items/9999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Item with id 9999 not found"})

    def test_user_not_authorized(self):
        response = self.client.get("/admin")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {"detail": "User not authorized to perform this action"})

if __name__ == '__main__':
    unittest.main()

