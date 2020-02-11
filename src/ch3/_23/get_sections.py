import re
from os import linesep
from pathlib import Path
from typing import Iterator
from typing import Tuple

from src.ch3._20.ndjson import parse

_section_regex = re.compile(r"(?P<level>={2,}) (.+) (?P=level)")


def get_sections(article: str) -> Iterator[Tuple[int, str]]:
    return map(lambda m: (len(m[0]) - 1, m[1]), _section_regex.findall(article))


def main(filepath: str):
    with open(filepath, "r") as file:
        for data in parse(file):
            title = data["title"]
            article = data["text"]
            if type(article) == str and type(title) == str:
                categories = get_sections(article)
                print(title, *categories, sep=linesep)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filepath = str((workdir / "../jawiki-country.json").resolve())
    main(filepath)
