from argparse import ArgumentParser
from argparse import FileType
from contextlib import ExitStack
from itertools import islice
from pathlib import Path
from typing import IO
from typing import Iterator


def split(io_: IO[str], *, N: int = 1) -> Iterator[str]:
    blank = str()
    join = blank.join
    while True:
        block = join(islice(io_, N))
        if block == blank:
            break
        yield block


if __name__ == "__main__":
    parser = ArgumentParser(description="split a file into pieces")

    parser.add_argument("file", type=FileType("r"), default="-")
    parser.add_argument(
        "-l", metavar="line_count", type=int, help="Create smaller files n lines in length.",
    )

    args = parser.parse_args()
    workdir = Path(__file__).parent

    with ExitStack() as stack:
        for i, string in enumerate(split(args.file, N=args.l)):
            file = stack.enter_context(open(str(workdir / f"result_{i+1}"), "w"))
            file.write(string)
