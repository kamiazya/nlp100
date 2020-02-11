import sys
import unittest
from io import StringIO

from src.ch2._15.tail import tail


class TestTail(unittest.TestCase):
    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor
        self.io = StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n")

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.io.close()

    def test_tail(self):
        self.assertEqual(tail(self.io), "11\n")

    def test_tail_3(self):
        self.assertEqual(tail(self.io, n=3), "9\n10\n11\n")

    def test_tail_10(self):
        self.assertEqual(
            tail(self.io, n=10), "2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n",
        )


if __name__ == "__main__":
    unittest.main()
