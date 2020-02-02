from typing import List, Iterator


def n_gram(paragraph: str, *, n: int = 1) -> Iterator[str]:
    return map(lambda i: paragraph[i:i+n], range(len(paragraph)-n+1))


def bi_gram(paragraph: str) -> Iterator[str]:
    return n_gram(paragraph, n=2)


def word_n_gram(paragraph: str, *, n: int = 1) -> Iterator[str]:
    sep = " "
    words = paragraph.split(sep)
    return map(lambda i: sep.join(words[i:i+n]), range(len(words)-n+1))


def word_bi_gram(paragraph: str) -> Iterator[str]:
    return word_n_gram(paragraph, n=2)


def main() -> Iterator[str]:
    paragraph: str = "I am an NLPer"
    return word_bi_gram(paragraph)


if __name__ == '__main__':
    result: List[str] = list(main())
    print(result)
