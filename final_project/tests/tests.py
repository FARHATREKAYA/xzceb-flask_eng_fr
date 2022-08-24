import unittest

from machinetranslation import translator


class EnglishToFrenchTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.englishToFrench(''), '')
        self.assertEqual(translator.englishToFrench('Hello'),'Bonjour')


class FrenchToEnglishTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.frenchToEnglish(''),'')

        self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')

unittest.main()