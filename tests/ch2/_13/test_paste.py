import subprocess
from contextlib import ExitStack
from pathlib import Path

from src.ch2._13.paste import paste


def test_paste():
    result = paste(["a", "b", "c"], ["1", "2", "3"])

    assert result == "a\t1\nb\t2\nc\t3\n"


def test_paste_space_delimiter():
    result = paste(["a", "b", "c"], ["1", "2", "3"], delimiter=" ")

    assert result == "a 1\nb 2\nc 3\n"


def test_paste_with_command():
    workdir = Path(__file__).parent
    with ExitStack() as stack:
        filepaths = list(
            map(lambda i: str((workdir / f"../../../src/ch2/_12/col{i}.txt").resolve()), [1, 2],)
        )

        col1, col2 = map(lambda filepath: stack.enter_context(open(filepath, "r")), filepaths)

        expected = subprocess.check_output(f"paste {' '.join(filepaths)}", shell=True).decode()

        assert paste(col1, col2) == expected
