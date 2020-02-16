import pytest

from src.ch3._25.get_base_infomation import get_base_infomation_items


@pytest.mark.parametrize(
    "content,expected",
    [
        ("基礎情報", {}),
        ("基礎情報|a=1 |b = 2|", {"a": "1", "b": "2"}),
        ("基礎情報|a=1 |b = 2|c =3", {"a": "1", "b": "2", "c": "3"}),
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
        (
            (
                """
                {{基礎情報 国 |
                    a=1 |
                    b = {{hoge | fuga}} |
                    c ={{foo | var}}
                }}"""
            ),
            {"a": "1", "b": "{{hoge | fuga}}", "c": "{{foo | var}}"},
        ),
        (
            (
                """
                {{基礎情報 国
                    | a=1
                    | b = {{hoge | fuga}}
                    | c ={{foo | var}}
                }}"""
            ),
            {"a": "1", "b": "{{hoge | fuga}}", "c": "{{foo | var}}"},
        ),
    ],
)
def test_get_base_infomation_items(content, expected):
    assert get_base_infomation_items(content) == expected
