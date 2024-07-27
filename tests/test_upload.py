import unittest
from your_flask_app import app

class TestUpload(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_file(self):
        with open('path/to/your/test/file.txt', 'rb') as file:
            response = self.app.post('/upload', data={'file': file})
        self.assertEqual(response.status_code, 200)
        self.assertIn('File uploaded successfully', response.data.decode())

if __name__ == "__main__":
    unittest.main()

