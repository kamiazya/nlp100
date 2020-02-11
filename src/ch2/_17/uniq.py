from os import linesep
from pathlib import Path
from typing import Iterable
from typing import Set


def uniq(words: Iterable[str]) -> Set[str]:
    return {*words}


def main(filename: str):
    with open(filename, "r") as file:
        words = map(lambda l: l.split("\t")[0].strip(), file)
        print(*sorted(uniq(words)), sep=linesep)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filename = str((workdir / "../hightemp.txt").resolve())
    main(filename)
