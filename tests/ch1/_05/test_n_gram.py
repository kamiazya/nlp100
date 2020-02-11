from src.ch1._05.n_gram import bi_gram
from src.ch1._05.n_gram import main
from src.ch1._05.n_gram import n_gram
from src.ch1._05.n_gram import word_bi_gram
from src.ch1._05.n_gram import word_n_gram


def test_main():
    assert list(main()) == ["I am", "am an", "an NLPer"]


def test_n_gram():
    paragraph: str = "I am an NLPer"
    assert list(n_gram(paragraph)) == [
        "I",
        " ",
        "a",
        "m",
        " ",
        "a",
        "n",
        " ",
        "N",
        "L",
        "P",
        "e",
        "r",
    ]


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


def test_n_gram_3():
    paragraph: str = "I am an NLPer"
    assert list(n_gram(paragraph, n=3)) == [
        "I a",
        " am",
        "am ",
        "m a",
        " an",
        "an ",
        "n N",
        " NL",
        "NLP",
        "LPe",
        "Per",
    ]


def test_word_n_gram():
    paragraph: str = "I am an NLPer"
    assert list(word_n_gram(paragraph)) == ["I", "am", "an", "NLPer"]


def test_word_bi_gram():
    paragraph: str = "I am an NLPer"
    assert list(word_bi_gram(paragraph)) == ["I am", "am an", "an NLPer"]


def test_word_n_gram_3():
    paragraph: str = "I am an NLPer"
    assert list(word_n_gram(paragraph, n=3)) == ["I am an", "am an NLPer"]
