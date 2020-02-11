import re
from os import linesep
from pathlib import Path
from typing import List

from src.ch3._20.ndjson import parse

_categories_regex = re.compile(r"\[\[Category:(.+)\]\]")


def get_categories(article: str) -> List[str]:
    return _categories_regex.findall(article)


def main(filepath: str):
    with open(filepath, "r") as file:
        for data in parse(file):
            title = data["title"]
            article = data["text"]
            if type(article) == str and type(title) == str:
                categories = get_categories(article)

                print(title, *categories, sep=linesep)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filepath = str((workdir / "../jawiki-country.json").resolve())
    main(filepath)
