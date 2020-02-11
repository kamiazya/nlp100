import sys
import unittest
from io import StringIO

from src.ch2._14.head import head


class TestHead(unittest.TestCase):
    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor
        self.io = StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n")

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.io.close()

    def test_head(self):
        self.assertEqual(head(self.io), "1\n")

    def test_head_3(self):
        self.assertEqual(head(self.io, n=3), "1\n2\n3\n")

    def test_head_10(self):
        self.assertEqual(
            head(self.io, n=10), "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n",
        )


if __name__ == "__main__":
    unittest.main()
