# tests/test_ocr.py

import unittest
from app.controllers.ocr import ocr_extraction
from unittest.mock import patch, MagicMock

class TestOCR(unittest.TestCase):
    @patch('app.controllers.ocr.Image.open')
    @patch('app.controllers.ocr.image_to_string')
    def test_ocr_extraction(self, mock_image_to_string, mock_image_open):
        mock_image_to_string.return_value = "This is a test text."
        mock_image_open.return_value = MagicMock()
        result = ocr_extraction("path/to/test/image.png")
        self.assertEqual(result, "This is a test text.")

if __name__ == '__main__':
    unittest.main()

