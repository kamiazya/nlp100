import re
from os import linesep
from pathlib import Path
from typing import IO

from src.ch3._20.ndjson import parse


_base_infomation_patten = r"\{\{基礎情報.+?$(.+?)\}\}"
_base_infomation_item_patten = r"\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))"
_base_infomation_regex = re.compile(_base_infomation_patten, re.MULTILINE | re.VERBOSE | re.DOTALL)
_base_infomation_item_regex = re.compile(_base_infomation_item_patten, re.MULTILINE + re.DOTALL)


#  -> Dict[str, str]
def get_base_infomation(article: str):
    m = _base_infomation_regex.match(article)
    if m:
        return dict(_base_infomation_item_regex.findall(m.group(0)))
    return {}


def main(file: IO[str]):
    # data = next(parse(file))
    for data in parse(file):
        title = data["title"]
        article = data["text"]
        if type(article) is str and type(title) is str:
            info = get_base_infomation(article)
            print(title, info, sep=linesep)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filepath = str((workdir / "../jawiki-country.json").resolve())
    with open(filepath, "r") as file:
        main(file)
