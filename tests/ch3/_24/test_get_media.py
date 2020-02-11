import pytest

from src.ch3._24.get_media import get_media


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
                "[[ファイル:All Gizah Pyramids.jpg|thumb|300px|right|[[ギーザ|ギザ]]の[[三大ピラミッド]]。]]\n"
                "== め ==\n"
                "[[Category:カフカス]]\n"
                "[[ファイル:Egyptiska hieroglyfer, Nordisk familjebok.png|thumb|260px|right|[[ヒエログリフ]]。]]\n"
                "[[Category:オセット]]\n"
            ),
            ["All Gizah Pyramids.jpg", "Egyptiska hieroglyfer, Nordisk familjebok.png"],
        ),
        (
            (
                "あい\n"
                "[[Category:日本|*]]\n"
                "== うえ ==\n"
                "[[Category:島国]]\n"
                "[[ファイル:Hosni Mubarak ritratto.jpg|thumb|left|[[アラブの春]]で失脚するまで30年以上に渡り長期政権を維持した[[ホスニー・ムバーラク]]]]\n"
                "お\n"
                "[[Category:君主国]]\n"
                "== かき く ==\n"
                "かきくけこ\n"
                "======= いろは =======\n"
                "[[Category:G8加盟国]]\n"
            ),
            ["Hosni Mubarak ritratto.jpg"],
        ),
    ],
)
def test_get_section(article, expected):
    assert [*get_media(article)] == expected
