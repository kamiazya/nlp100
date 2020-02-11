import sys
import unittest
from src.ch2._15.tail import tail
from io import StringIO


class TestTail(unittest.TestCase):
    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor
        self.io = StringIO(("1\n" "2\n" "3\n" "4\n" "5\n" "6\n" "7\n" "8\n" "9\n" "10\n" "11\n"))

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.io.close()

    def test_tail(self):
        self.assertEqual(tail(self.io), "11\n")

    def test_tail_3(self):
        self.assertEqual(tail(self.io, n=3), ("9\n" "10\n" "11\n"))

    def test_tail_10(self):
        self.assertEqual(
            tail(self.io, n=10), ("2\n" "3\n" "4\n" "5\n" "6\n" "7\n" "8\n" "9\n" "10\n" "11\n"),
        )


if __name__ == "__main__":
    unittest.main()
