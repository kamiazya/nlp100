import sys
import unittest
from io import StringIO
from src.ch1._03.pi import main, format_word


class TestPi(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_format_word(self):
        cases = [
            ("hoge.", "hoge"),
            ("hoge,", "hoge"),
            ("hoge", "hoge"),
        ]
        for (input_, output) in cases:
            self.assertEqual(format_word(input_), output)

    def test_main(self):
        self.assertEqual(main(),
                         [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9])


if __name__ == '__main__':
    unittest.main()
