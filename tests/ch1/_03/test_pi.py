import pytest

from src.ch1._03.pi import format_word
from src.ch1._03.pi import main


@pytest.mark.parametrize(
    "input_,expected", [("hoge.", "hoge"), ("hoge,", "hoge"), ("hoge", "hoge")]
)
def test_format_word(input_, expected):
    assert format_word(input_) == expected


def test_main():
    assert main() == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
