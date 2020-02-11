from src.ch1._06.bi_gram import DIFFERENCE
from src.ch1._06.bi_gram import INTERSECTION
from src.ch1._06.bi_gram import UNION
from src.ch1._06.bi_gram import X_HAS_SE
from src.ch1._06.bi_gram import Y_HAS_SE
from src.ch1._06.bi_gram import X
from src.ch1._06.bi_gram import Y
from src.ch1._06.bi_gram import bi_gram


def test_bi_gram():
    paragraph: str = "I am an NLPer"
    assert list(bi_gram(paragraph)) == [
        "I ",
        " a",
        "am",
        "m ",
        " a",
        "an",
        "n ",
        " N",
        "NL",
        "LP",
        "Pe",
        "er",
    ]


def test_X():
    assert X == {"ap", "pa", "is", "se", "ra", "ar", "di", "ad"}


def test_Y():
    assert Y == {"ap", "ph", "gr", "ag", "pa", "ra", "ar"}


def test_UNION():
    assert UNION == {"ap", "ph", "gr", "ag", "pa", "is", "se", "ra", "ar", "di", "ad"}


def test_INTERSECTION():
    assert INTERSECTION == {"ap", "ar", "pa", "ra"}


def test_DIFFERENCE():
    assert DIFFERENCE == {"is", "se", "di", "ad"}


def test_X_HAS_SE():
    assert X_HAS_SE is True


def test_Y_HAS_SE():
    assert Y_HAS_SE is False
