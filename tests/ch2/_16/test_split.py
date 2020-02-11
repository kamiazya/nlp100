from io import StringIO

import pytest

from src.ch2._16.split import split


@pytest.fixture
def stdin():
    return StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n")


def test_split(stdin):
    assert list(split(stdin)) == [
        "1\n",
        "2\n",
        "3\n",
        "4\n",
        "5\n",
        "6\n",
        "7\n",
        "8\n",
        "9\n",
        "10\n",
        "11\n",
    ]


@pytest.mark.parametrize(
    "N,expected",
    [
        (3, ["1\n2\n3\n", "4\n5\n6\n", "7\n8\n9\n", "10\n11\n"]),
        (10, ["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n", "11\n"]),
    ],
)
def test_split_n(stdin, N, expected):
    assert list(split(stdin, N=N)) == expected
