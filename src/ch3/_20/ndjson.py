import json
from pathlib import Path
from typing import Any
from typing import Generator
from typing import Iterable

from src.ch3._20.find_one import find_one


def parse(json_lines: Iterable[str]) -> Generator[Any, None, None]:
    for line in json_lines:
        yield json.loads(line)


def main(filepath: str):
    def _is_english_article(data: Any) -> bool:
        return isinstance(data, dict) and data["title"] == "イギリス"

    with open(filepath) as file:
        data = find_one(parse(file), _is_english_article)
        if data is not None:
            print(data["text"])


if __name__ == "__main__":
    workdir = Path(__file__).parent
    filepath = str((workdir / "../jawiki-country.json").resolve())
    main(filepath)
