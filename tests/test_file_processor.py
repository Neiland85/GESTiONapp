import unittest
from app.controllers.file_processor import process_file, save_file

class TestFileProcessor(unittest.TestCase):

    def test_process_file(self):
        # Create a mock file object
        class MockFile:
            def __init__(self, filename, content):
                self.filename = filename
                self.content = content
            def file(self):
                return self

            def read(self):
                return self.content

        file = MockFile("test.txt", b"dummy content")
        result = process_file(file)
        self.assertEqual(result["status"], "processed")
        self.assertEqual(result["filename"], "test.txt")

if __name__ == "__main__":
    unittest.main()

