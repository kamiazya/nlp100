import pytest

from src.ch3._22.categories import get_categories


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
            ["南オセチア|*", "グルジアの地理", "カフカス", "オセット"],
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
            ["日本|*", "島国", "君主国", "G8加盟国"],
        ),
    ],
)
def test_get_categories(article, expected):
    assert get_categories(article) == expected
