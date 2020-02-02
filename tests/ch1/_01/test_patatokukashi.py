import sys
import unittest
from io import StringIO


class TestPatatokukashi(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_reverse_word(self):
        import src.ch1._01.patatokukashi  # NOQA
        self.captor.seek(0)
        self.assertEqual(self.captor.read(), "タクシー\n")


if __name__ == '__main__':
    unittest.main()
