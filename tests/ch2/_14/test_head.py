import sys
import unittest
from src.ch2._14.head import head
from io import StringIO


class TestHead(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor
        self.io = StringIO((
            "1\n"
            "2\n"
            "3\n"
            "4\n"
            "5\n"
            "6\n"
            "7\n"
            "8\n"
            "9\n"
            "10\n"
            "11\n"
        ))

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.io.close()

    def test_head(self):
        self.assertEqual(head(self.io), "1\n")

    def test_head_3(self):
        self.assertEqual(head(self.io, n=3), (
            "1\n"
            "2\n"
            "3\n"
        ))

    def test_head_10(self):
        self.assertEqual(head(self.io, n=10), (
            "1\n"
            "2\n"
            "3\n"
            "4\n"
            "5\n"
            "6\n"
            "7\n"
            "8\n"
            "9\n"
            "10\n"
        ))


if __name__ == "__main__":
    unittest.main()
