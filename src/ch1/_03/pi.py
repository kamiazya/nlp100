from functools import reduce
from typing import List

noise_chars: List[str] = [",", "."]


def format_word(word: str) -> str:
    return reduce(lambda w, sep: w.rstrip(sep), noise_chars, word)


def main() -> List[int]:
    paragraph = (
        "Now I need a drink, alcoholic of course, "
        "after the heavy lectures involving quantum mechanics."
    )
    return list(map(len, map(format_word, paragraph.split(" "))))


if __name__ == "__main__":
    result = main()
    print(result)
