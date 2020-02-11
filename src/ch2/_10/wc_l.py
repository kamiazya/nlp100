from contextlib import ExitStack
from pathlib import Path


def wc_l(*filepath: str) -> int:
    c = 0
    with ExitStack() as stack:
        for fp in filepath:
            f = stack.enter_context(open(fp, "r"))
            c += sum([1 for _ in f])
    return c


if __name__ == "__main__":
    filename = str((Path(__file__) / "../../hightemp.txt").resolve())
    print(wc_l(filename))
