import pytest

from src.ch2._19.sort_hist import sort_hist


@pytest.mark.parametrize(
    "words,expected",
    [
        ("AABAA", ["A", "B"]),
        ("AABAABBBB", ["B", "A"]),
        (
            ["a", "I", "pen", "I", "I", "I", "I", "I", "have", "have", "have", "have", "a", "I"],
            ["I", "have", "a", "pen"],
        ),
    ],
)
def test_sort_hist(words, expected):
    assert [*sort_hist(words)] == expected
