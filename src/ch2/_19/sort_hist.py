from functools import cached_property
from operator import itemgetter
from os import linesep
from pathlib import Path
from typing import Iterator


class _hist_ordered(dict):
    def __init__(self, keys: Iterator[str]) -> None:
        for key in keys:
            self[key] += 1

    def __missing__(self, key):
        return 0

    @cached_property
    def ordered_keys(self) -> Iterator[str]:
        return map(
            itemgetter(1),
            sorted(map(lambda k: (self[k], k), self.keys()), reverse=True, key=itemgetter(0)),
        )


def sort_hist(words: Iterator[str]) -> Iterator[str]:
    return _hist_ordered(words).ordered_keys


def main(filename: str):
    with open(filename, "r") as file:
        words = map(lambda l: l.split("\t")[0].strip(), file)
        print(*sort_hist(words), sep=linesep)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filename = str((workdir / "../hightemp.txt").resolve())
    main(filename)
