import sys
from pathlib import Path
from select import select
from contextlib import ExitStack


def is_pipe():
    if select([sys.stdin, ], [], [], 0.0)[0]:
        return True
    return False


def wc_l(*filepath: str) -> int:
    c = 0
    with ExitStack() as stack:
        for fp in filepath:
            f = stack.enter_context(open(fp, 'r'))
            c += sum([1 for _ in f])
    return c


if __name__ == "__main__":
    filename = str((Path(__file__) / "../../hightemp.txt").resolve())
    print(wc_l(filename))
