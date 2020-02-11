def test_reverse_word(capfd):
    import src.ch1._00.reverse_word  # NOQA

    captured = capfd.readouterr()
    assert captured.out == "desserts\n"
