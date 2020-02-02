from typing import List, Iterator
from functools import reduce

noise_chars: List[str] = [",", "."]


def format_word(word: str) -> str:
    return reduce(lambda w, sep: w.rstrip(sep), noise_chars, word)


def main() -> List[int]:
    paragraph: str = (
        "Now I need a drink, alcoholic of course,"
        " after the heavy lectures involving quantum mechanics."
    )
    words: Iterator[str] = map(format_word, paragraph.split(" "))
    return list(map(lambda w: len(w), words))


if __name__ == '__main__':
    result = main()
    print(result)
