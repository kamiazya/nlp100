import sys
import unittest
from io import StringIO


class TestPatokaTakushi(unittest.TestCase):
    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_patoka_takushi(self):
        import src.ch1._02.patoka_takushi  # NOQA

        self.captor.seek(0)
        self.assertEqual(self.captor.read(), "パタトクカシーー\n")


if __name__ == "__main__":
    unittest.main()
