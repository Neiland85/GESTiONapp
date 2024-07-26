# tests/test_government_api.py

import unittest
from app.controllers.government_api import enviar_datos_gobierno
from unittest.mock import patch

class TestGovernmentAPI(unittest.TestCase):
    @patch('app.controllers.government_api.requests.post')
    def test_enviar_datos_gobierno(self, mock_post):
        mock_post.return_value.json.return_value = {"status": "success"}
        data = {"id": 1, "name": "Test"}
        result = enviar_datos_gobierno(data)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["status"], "success")

if __name__ == '__main__':
    unittest.main()

