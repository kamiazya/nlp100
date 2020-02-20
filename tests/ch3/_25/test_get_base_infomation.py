import pytest

from src.ch3._25.get_base_infomation import get_base_infomation


@pytest.mark.parametrize(
    "article,expected",
    [
        ("記事", None),
        ("{{基礎情報|a=1 |b = 2}}", {"a": "1", "b": "2"}),
        ("{{基礎情報|a=1 |b = 2|c =3}}", {"a": "1", "b": "2", "c": "3"}),
        (
            (
                """
                {{基礎情報 国
                    |a=1
                    |b = 2
                }}"""
            ),
            {"a": "1", "b": "2"},
        ),
        (
            (
                """
                {{基礎情報 国 |
                    a=1 |
                    b = 2
                }}"""
            ),
            {"a": "1", "b": "2"},
        ),
        (
            (
                """
                {{基礎情報 国 |
                    a=1 |
                    b = {{hoge | fuga}}
                }}"""
            ),
            {"a": "1", "b": "{{hoge | fuga}}"},
        ),
    ],
)
def test_get_base_infomation(article, expected):
    assert get_base_infomation(article) == expected
