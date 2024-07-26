# tests/test_file_processor.py

import unittest
from app.controllers.file_processor import process_file
from fastapi import UploadFile
from io import BytesIO

class MockUploadFile(UploadFile):
    def __init__(self, filename, content):
        super().__init__(filename=filename, file=BytesIO(content.encode()))

class TestFileProcessor(unittest.TestCase):
    def test_process_file(self):
        mock_file = MockUploadFile(filename="test.txt", content="This is a test file.")
        result = process_file(mock_file)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["status"], "processed")

if __name__ == '__main__':
    unittest.main()

