import subprocess
from pathlib import Path

import pytest

from src.ch2._12.cut import cut


@pytest.mark.parametrize("i", range(1, 5))
def test_cut(i):
    filename = str((Path(__file__) / "../../../../src/ch2/hightemp.txt").resolve())
    result = cut(filename, f=i)
    command = f"cut -f {i} {filename}"
    check_cut = subprocess.check_output(command, shell=True)
    assert result == check_cut.decode()
