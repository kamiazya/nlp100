from pathlib import Path
from typing import IO
from typing import Dict
from typing import Optional

import regex

from src.ch3._20.ndjson import parse

_base_infomation_regex = regex.compile(
    r"(?<rec>\{\{((?:[^\{\}]+|(?&rec))*)\}\})", flags=(regex.MULTILINE),
)

_base_infomation_item_regex = regex.compile(
    r"(?<=[\|^])(.+?)\s*=\s*((\{\{.+?\}\})|(.+?))(?=[\|$]?)",
    flags=(regex.MULTILINE + regex.DOTALL),
)


def get_base_infomation_items(content: str) -> Dict[str, str]:
    return {
        m.group(1).strip(): m.group(2).strip()
        for m in _base_infomation_item_regex.finditer(content)
    }


def get_base_infomation(text: str) -> Optional[Dict[str, str]]:
    result = _base_infomation_regex.finditer(text)
    if result:
        for r in result:
            content: str = r.group(2)
            if content.startswith("基礎情報"):
                return get_base_infomation_items(content)
    return None


def main(file: IO[str]):
    result = {}
    for data in parse(file):
        title = data["title"]
        article = data["text"]
        if type(article) is str and type(title) is str:
            info = get_base_infomation(article)
            if info is not None:
                result[title] = info
    print(result)


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filepath = str((workdir / "../jawiki-country.json").resolve())
    with open(filepath, "r") as file:
        main(file)
