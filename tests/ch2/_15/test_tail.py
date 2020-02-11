from io import StringIO

import pytest

from src.ch2._15.tail import tail


@pytest.fixture
def stdin():
    return StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n")


def test_tail(stdin):
    assert tail(stdin) == "11\n"


@pytest.mark.parametrize(
    "expected,n", [("9\n10\n11\n", 3), ("2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n", 10)]
)
def test_tail_n(stdin, expected, n):
    assert tail(stdin, n=3) == "9\n10\n11\n"
