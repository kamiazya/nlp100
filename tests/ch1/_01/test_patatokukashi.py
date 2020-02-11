def test_patatokukashi(capfd):
    import src.ch1._01.patatokukashi  # NOQA

    captured = capfd.readouterr()

    assert captured.out == "タクシー\n"


def test_patatokukashi_use_slice(capfd):
    import src.ch1._01.patatokukashi_use_slice  # NOQA

    captured = capfd.readouterr()
    assert captured.out == "タクシー\n"
