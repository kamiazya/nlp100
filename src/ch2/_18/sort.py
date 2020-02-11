from operator import itemgetter
from os import linesep
from pathlib import Path
from typing import Iterator


def sort(words: Iterator[str]) -> Iterator[str]:
    return map(
        itemgetter(0), sorted(map(lambda w: (w, float(w)), words), key=itemgetter(1), reverse=True),
    )


def main(filename: str):
    with open(filename, "r") as file:
        words = map(lambda l: l.split("\t")[2].strip(), file)
        print(*sort(words), sep=linesep)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filename = str((workdir / "../hightemp.txt").resolve())
    main(filename)
