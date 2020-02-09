from os import linesep
from contextlib import ExitStack
from pathlib import Path
from typing import Iterable


def paste(*lines: Iterable[str], delimiter: str = "\t"):
    return linesep.join(
        map(lambda l: delimiter.join(
            map(lambda w: w.strip(), l)),
            zip(*lines))) + linesep


if __name__ == "__main__":
    filename = str((Path(__file__) / "../../hightemp.txt").resolve())

    workdir = Path(__file__).parent
    with ExitStack() as stack:
        col1, col2 = map(lambda i: stack.enter_context(
            open(str((workdir / f"../_12/col{i}.txt").resolve()), "r")),
            [1, 2])

        file = stack.enter_context(
            open(str((workdir / "result.txt").resolve()), "w"))

        file.write(paste(col1, col2))
