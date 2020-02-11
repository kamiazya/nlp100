import subprocess
from pathlib import Path

from src.ch2._10.wc_l import wc_l


def test_wc_l():
    filename = str((Path(__file__) / "../../../../src/ch2/hightemp.txt").resolve())
    result = wc_l(filename)
    command = f"cat {filename} | wc -l | awk " + "'{print $1}'"
    check_wc = subprocess.check_output(command, shell=True)
    assert result == int(check_wc)
