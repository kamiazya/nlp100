from src.ch1._09.typoglycemia import shuffle_paragraph


def test_typoglycemia():
    result = shuffle_paragraph("aBCDEf")
    chars = list(result)
    length: int = len(chars)
    assert chars[0] == "a"
    assert {*chars[1 : length - 1]} == {*"BCDE"}
    assert chars[length - 1] == "f"


def test_typoglycemia_length_4():
    result = shuffle_paragraph("abcd")
    assert result == "abcd"


def test_typoglycemia_mixed():
    word1, word2 = shuffle_paragraph("abcd aBCDEf").split(" ")
    assert word1 == "abcd"
    chars = list(word2)
    length: int = len(chars)
    assert chars[0] == "a"
    assert {*chars[1 : length - 1]} == {*"BCDE"}
    assert chars[length - 1] == "f"
