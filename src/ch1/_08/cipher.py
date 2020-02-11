from typing import Set, Callable


_lowercase_letters: Set[int] = {*range(ord("a"), ord("z") + 1)}

_cipher_magic_number: int = 219


def _encode(c: int) -> int:
    return _cipher_magic_number - c if c in _lowercase_letters else c


def _decode(c: int) -> int:
    return _cipher_magic_number - c if _cipher_magic_number - c in _lowercase_letters else c


def _cipher(converter: Callable[[int], int]) -> Callable[[str], str]:
    return lambda string: "".join(map(chr, map(converter, map(ord, string))))


encode: Callable[[str], str] = _cipher(_encode)
decode: Callable[[str], str] = _cipher(_decode)


if __name__ == "__main__":
    result = encode("hoge")
    print(decode(result))
