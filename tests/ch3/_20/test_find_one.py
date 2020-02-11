import pytest

from src.ch3._20.find_one import find_one


@pytest.mark.parametrize(
    "it,func,expected",
    [
        ("AABAA", lambda w: w == "A", "A"),
        ("AABAA", lambda w: w == "B", "B"),
        (range(10), lambda i: i > 5, 6),
    ],
)
def test_find_one(it, func, expected):
    assert find_one(it, func) == expected
