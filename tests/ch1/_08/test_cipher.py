import unittest
from src.ch1._08.cipher import encode, decode


class TestCipher(unittest.TestCase):

    def test_encode_decode(self):
        cases = [
            ("hoge", "sltv"),
            ("I have a pen", "I szev z kvm"),
            ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"),
        ]

        for (string, expected_encoded) in cases:
            encoded = encode(string)
            self.assertEqual(encoded, expected_encoded)
            self.assertEqual(decode(encoded), string)


if __name__ == "__main__":
    unittest.main()
