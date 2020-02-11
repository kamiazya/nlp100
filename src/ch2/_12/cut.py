from os import linesep
from pathlib import Path
from typing import Optional


def cut(filename: str, *, f: int, d: Optional[str] = "\t") -> str:
    with open(filename, "r") as file:
        return linesep.join(map(lambda line: line.rstrip().split(d)[f - 1], file)) + linesep


if __name__ == "__main__":
    filename = str((Path(__file__) / "../../hightemp.txt").resolve())

    workdir = Path(__file__).parent

    for i in [1, 2]:
        with open(str((workdir / f"col{i}.txt").resolve()), "w") as output:
            output.write(cut(filename, f=i))
