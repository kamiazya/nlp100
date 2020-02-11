def test_patoka_takushi(capfd):
    import src.ch1._02.patoka_takushi  # NOQA

    captured = capfd.readouterr()

    assert captured.out == "パタトクカシーー\n"
