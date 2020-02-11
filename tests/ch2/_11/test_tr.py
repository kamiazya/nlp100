import subprocess
from pathlib import Path

from src.ch2._11.tr import tr


def test_tr():
    filename = str((Path(__file__) / "../../../../src/ch2/hightemp.txt").resolve())
    result = tr("\t", " ", filename)
    command = f"cat {filename} | tr '\\t' ' '"
    check_tr = subprocess.check_output(command, shell=True)
    assert result == check_tr.decode()
