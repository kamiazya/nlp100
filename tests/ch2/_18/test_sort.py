import subprocess
from pathlib import Path

import pytest

from src.ch2._18.sort import main
from src.ch2._18.sort import sort


@pytest.mark.parametrize(
    "words,expected",
    [
        (["123", "1"], ["123", "1"]),
        (["1.5", "123", "1"], ["123", "1.5", "1"]),
        (["1.5", "-1", "123", "1"], ["123", "1.5", "1", "-1"]),
    ],
)
def test_uniq(words, expected):
    assert [*sort(words)] == expected


def test_main(capfd):
    filename = str(Path(__file__).parent / "../../../src/ch2/hightemp.txt")
    expected = subprocess.check_output(
        f"cat {filename} | cut -f 3 - | sort -r", shell=True
    ).decode()

    main(filename)

    captured = capfd.readouterr()
    assert {*captured.out.split("\n")} == {*expected.split("\n")}
