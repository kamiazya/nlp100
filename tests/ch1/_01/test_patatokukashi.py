import sys
import unittest
from io import StringIO


class TestPatatokukashi(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_patatokukashi(self):
        import src.ch1._01.patatokukashi  # NOQA
        self.captor.seek(0)
        self.assertEqual(self.captor.read(), "タクシー\n")

    def test_patatokukashi_use_slice(self):
        import src.ch1._01.patatokukashi_use_slice  # NOQA
        self.captor.seek(0)
        self.assertEqual(self.captor.read(), "タクシー\n")


if __name__ == '__main__':
    unittest.main()
