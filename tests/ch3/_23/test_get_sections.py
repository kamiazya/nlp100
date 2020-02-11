import pytest

from src.ch3._23.get_sections import get_sections


@pytest.mark.parametrize(
    "article,expected",
    [
        (
            (
                "あい\n"
                "ue\n"
                "== あ ==\n"
                "\n"
                "お\n"
                "=== お ===\n"
                "[[Category:南オセチア|*]]\n"
                "[[Category:グルジアの地理]]\n"
                "== め ==\n"
                "[[Category:カフカス]]\n"
                "[[Category:オセット]]\n"
            ),
            [(1, "あ"), (2, "お"), (1, "め")],
        ),
        (
            (
                "あい\n"
                "[[Category:日本|*]]\n"
                "== うえ ==\n"
                "[[Category:島国]]\n"
                "お\n"
                "[[Category:君主国]]\n"
                "== かき く ==\n"
                "かきくけこ\n"
                "======= いろは =======\n"
                "[[Category:G8加盟国]]\n"
            ),
            [(1, "うえ"), (1, "かき く"), (6, "いろは")],
        ),
    ],
)
def test_get_section(article, expected):
    assert [*get_sections(article)] == expected
