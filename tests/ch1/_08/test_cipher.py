import pytest

from src.ch1._08.cipher import decode
from src.ch1._08.cipher import encode


@pytest.mark.parametrize(
    "string,expected_encoded",
    [
        ("hoge", "sltv"),
        ("I have a pen", "I szev z kvm"),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"),
    ],
)
def test_encode_decode(string, expected_encoded):
    encoded = encode(string)
    assert encoded == expected_encoded
    assert decode(encoded) == string
