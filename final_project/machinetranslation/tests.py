import unittest
from translator import english_to_french,french_to_english


class TestTranslator(unittest.TestCase):
    def test_en_fr_one(self):
        self.assertEqual(english_to_french(""),"")

    def test_fr_en_two(self):
        self.assertEqual(french_to_english(""),"")

    def test_en_fr_two(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test_fr_en_two(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")


if __name__ == "__main__":
    unittest.main()

