import subprocess
from pathlib import Path
import pytest

from src.ch2._17.uniq import uniq, main


@pytest.mark.parametrize(
    "string,uniqed",
    [
        ("123", {*"123"}),
        (["I", "have", "a", "pen"], {"I", "have", "a", "pen"}),
        (["a", "b", "a", "b"], {"a", "b"}),
        (["hoge", "fuga", "hoge", "fuga"], {"hoge", "fuga"}),
        (["hoge", "fuga", "foo", "bar", "hoge", "fuga"], {"hoge", "fuga", "foo", "bar"}),
    ],
)
def test_uniq(string, uniqed):
    assert uniq(string) == uniqed


def test_main(capfd):
    filename = str(Path(__file__).parent / "../../../src/ch2/hightemp.txt")
    expected = subprocess.check_output(f"cat {filename} | cut -f 1 - | uniq", shell=True).decode()

    main(filename)

    captured = capfd.readouterr()
    assert {*captured.out.split("\n")} == {*expected.split("\n")}
