import unittest
from src.ch1._05.n_gram import main, n_gram, bi_gram, word_n_gram, word_bi_gram


class TestNGram(unittest.TestCase):
    def test_main(self):
        self.assertEqual(list(main()), ["I am", "am an", "an NLPer"])

    def test_n_gram(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(
            list(n_gram(paragraph)), ["I", " ", "a", "m", " ", "a", "n", " ", "N", "L", "P", "e", "r"],
        )

    def test_bi_gram(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(
            list(bi_gram(paragraph)), ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL", "LP", "Pe", "er"],
        )

    def test_n_gram_3(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(
            list(n_gram(paragraph, n=3)),
            ["I a", " am", "am ", "m a", " an", "an ", "n N", " NL", "NLP", "LPe", "Per",],
        )

    def test_word_n_gram(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(list(word_n_gram(paragraph)), ["I", "am", "an", "NLPer"])

    def test_word_bi_gram(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(list(word_bi_gram(paragraph)), ["I am", "am an", "an NLPer"])

    def test_word_n_gram_3(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(list(word_n_gram(paragraph, n=3)), ["I am an", "am an NLPer"])


if __name__ == "__main__":
    unittest.main()
