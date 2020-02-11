import pytest

from src.ch3._20.ndjson import parse


@pytest.mark.parametrize(
    "string,expected",
    [
        ("1", [1]),
        (["true", "false"], [True, False]),
        (["1", "2"], [1, 2]),
        (['""', '""'], ["", ""]),
        (['{"hoge": 100}', '{"fuga": 10.5}'], [{"hoge": 100}, {"fuga": 10.5}]),
    ],
)
def test_ndjson(string, expected):
    assert list(parse(string)) == expected
