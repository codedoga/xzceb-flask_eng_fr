import unittest
from machinetranslation.translator import english_french, french_english

class TestStringMethods(unittest.TestCase):
    englishText = "Hello"
    frenchText = "Bonjour"

    # test function to test equality of two value
    def test_french(self):
        firstValue = self.englishText
        secondValue = french_english(self.frenchText)
        self.assertEqual(firstValue, secondValue)

    def test_english(self):
        firstValue = english_french(self.englishText)
        secondValue = self.frenchText
        self.assertEqual(firstValue, secondValue)

    def test_nullfrench(self):
        firstValue = None
        secondValue = french_english(None)
        self.assertEqual(firstValue, secondValue)

    def test_nullenglish(self):
        firstValue = english_french(None)
        secondValue = None
        self.assertEqual(firstValue, secondValue)


if __name__ == '__main__':
    unittest.main()