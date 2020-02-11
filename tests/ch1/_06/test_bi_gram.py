import unittest
from src.ch1._06.bi_gram import (
    bi_gram,
    X,
    Y,
    UNION,
    INTERSECTION,
    DIFFERENCE,
    X_HAS_SE,
    Y_HAS_SE,
)


class TestBiGram(unittest.TestCase):
    def test_bi_gram(self):
        paragraph: str = "I am an NLPer"
        self.assertEqual(
            list(bi_gram(paragraph)),
            ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL", "LP", "Pe", "er"],
        )

    def test_X(self):
        self.assertEqual(X, {"ap", "pa", "is", "se", "ra", "ar", "di", "ad"})

    def test_Y(self):
        self.assertEqual(Y, {"ap", "ph", "gr", "ag", "pa", "ra", "ar"})

    def test_UNION(self):
        self.assertEqual(UNION, {"ap", "ph", "gr", "ag", "pa", "is", "se", "ra", "ar", "di", "ad"})

    def test_INTERSECTION(self):
        self.assertEqual(INTERSECTION, {"ap", "ar", "pa", "ra"})

    def test_DIFFERENCE(self):
        self.assertEqual(DIFFERENCE, {"is", "se", "di", "ad"})

    def test_X_HAS_SE(self):
        self.assertEqual(X_HAS_SE, True)

    def test_Y_HAS_SE(self):
        self.assertEqual(Y_HAS_SE, False)


if __name__ == "__main__":
    unittest.main()
