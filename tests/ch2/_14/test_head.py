from io import StringIO

import pytest

from src.ch2._14.head import head


@pytest.fixture
def stdin():
    return StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n")


def test_head(stdin):
    assert head(stdin) == "1\n"


@pytest.mark.parametrize("expected,n", [("1\n2\n3\n", 3), ("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n", 10)])
def test_head_n(stdin, expected: str, n: int):
    assert head(stdin, n=n) == expected
