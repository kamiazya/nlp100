from typing import Callable
from typing import Iterable
from typing import Optional
from typing import TypeVar

T = TypeVar("T")


def find_one(
    it: Iterable[T], func: Callable[[T], bool], *, default: Optional[T] = None
) -> Optional[T]:
    return next(filter(func, it), default)
