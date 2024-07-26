# tests/test_classifier.py

import unittest
from app.controllers.classifier import classify_document

class TestClassifier(unittest.TestCase):
    def test_classify_document(self):
        result = classify_document("This is a test document.")
        self.assertIsInstance(result, dict)
        self.assertIn("document_type", result)

if __name__ == '__main__':
    unittest.main()

