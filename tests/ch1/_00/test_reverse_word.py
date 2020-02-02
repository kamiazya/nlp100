import sys
import unittest
from io import StringIO


class TestRevarseSrting(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_reverse_word(self):
        import src.ch1._00.reverse_word  # NOQA
        self.captor.seek(0)
        self.assertEqual(self.captor.read(), "desserts\n")


if __name__ == '__main__':
    unittest.main()
