from typing import List
import random


def _shuffle_word(word: str) -> str:
    chars: List[str] = list(word)
    length: int = len(chars)
    if length <= 4:
        return word
    shuffle_container: List[str] = chars[1:length-1]
    random.shuffle(shuffle_container)
    return "".join([chars[0], *shuffle_container, chars[length-1]])


def shuffle_paragraph(paragraph: str) -> str:
    space = " "
    words = paragraph.split(space)
    return space.join(map(_shuffle_word, words))


if __name__ == "__main__":
    paragraph = "I couldn't believe that I could actually understand "\
                "what I was reading : the phenomenal power of the human mind ."

    print(shuffle_paragraph(paragraph))
