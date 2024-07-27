import unittest
from your_app import app

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_value_error(self):
        response = self.app.get('/example?cause=value_error')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Value error occurred', response.data.decode())

    def test_internal_error(self):
        response = self.app.get('/example?cause=internal_error')
        self.assertEqual(response.status_code, 500)
        self.assertIn('Internal server error', response.data.decode())

if __name__ == "__main__":
    unittest.main()

