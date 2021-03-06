from typing import List
from typing import Set
from typing import Tuple


def main():
    paragraph = (
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. "
        "New Nations Might Also Sign Peace Security Clause. "
        "Arthur King Can."
    )

    special_indexes: Set[int] = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    words: List[str] = paragraph.split(" ")

    def get_char(t: Tuple[int, str]) -> str:
        index, word = t
        char_len = 1 if (index + 1) in special_indexes else 2
        return word[0:char_len]

    return list(map(get_char, enumerate(words)))


if __name__ == "__main__":
    result = main()
    print(result)
