import unittest
from src.ch1._09.typoglycemia import shuffle_paragraph


class TestTypoglycemia(unittest.TestCase):

    def test_typoglycemia(self):
        result = shuffle_paragraph("aBCDEf")
        chars = list(result)
        length: int = len(chars)
        self.assertEqual(chars[0], "a")
        self.assertEqual({*chars[1:length-1]}, {*"BCDE"})
        self.assertEqual(chars[length-1], "f")

    def test_typoglycemia_length_4(self):
        result = shuffle_paragraph("abcd")
        self.assertEqual(result, "abcd")

    def test_typoglycemia_mixed(self):
        word1, word2 = shuffle_paragraph("abcd aBCDEf").split(" ")
        self.assertEqual(word1, "abcd")
        chars = list(word2)
        length: int = len(chars)
        self.assertEqual(chars[0], "a")
        self.assertEqual({*chars[1:length-1]}, {*"BCDE"})
        self.assertEqual(chars[length-1], "f")


if __name__ == "__main__":
    unittest.main()
