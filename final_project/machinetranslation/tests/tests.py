from translator import english_to_french, french_to_english
import unittest

class Test(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french(' '),' ')
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(' '),' ')
unittest.main()