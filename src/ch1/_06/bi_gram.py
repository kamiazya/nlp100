from typing import Set, Iterator


def bi_gram(paragraph: str) -> Iterator[str]:
    n = 2
    return map(lambda i: paragraph[i:i+n], range(len(paragraph)-n+1))


x: str = "paraparaparadise"
y: str = "paragraph"
X: Set[str] = set(bi_gram(x))
Y: Set[str] = set(bi_gram(y))

UNION: Set[str] = X | Y
INTERSECTION: Set[str] = X & Y
DIFFERENCE: Set[str] = X - Y

X_HAS_SE: bool = "se" in X
Y_HAS_SE: bool = "se" in Y
