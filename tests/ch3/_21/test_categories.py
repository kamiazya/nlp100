import pytest

from src.ch3._21.categories import get_category_lines


@pytest.mark.parametrize(
    "article,expected",
    [
        (
            (
                "あい\n"
                "ue\n"
                "\n"
                "お\n"
                "[[Category:南オセチア|*]]\n"
                "[[Category:グルジアの地理]]\n"
                "[[Category:カフカス]]\n"
                "[[Category:オセット]]\n"
            ),
            [
                "[[Category:南オセチア|*]]",
                "[[Category:グルジアの地理]]",
                "[[Category:カフカス]]",
                "[[Category:オセット]]",
            ],
        ),
        (
            (
                "あい\n"
                "[[Category:日本|*]]\n"
                "うえ\n"
                "[[Category:島国]]\n"
                "お\n"
                "[[Category:君主国]]\n"
                "かきくけこ\n"
                "[[Category:G8加盟国]]\n"
            ),
            ["[[Category:日本|*]]", "[[Category:島国]]", "[[Category:君主国]]", "[[Category:G8加盟国]]"],
        ),
    ],
)
def test_get_category_lines(article, expected):
    assert get_category_lines(article) == expected
