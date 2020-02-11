from typing import Callable, Iterable, Optional, TypeVar


T = TypeVar("T")


def find_one(
    it: Iterable[T], func: Callable[[T], bool], *, default: Optional[T] = None
) -> Optional[T]:
    return next(filter(func, it), default)
