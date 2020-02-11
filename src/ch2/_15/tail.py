from argparse import ArgumentParser
from argparse import FileType
from collections import deque
from sys import stdout
from typing import IO


def tail(io_: IO[str], *, n: int = 1) -> str:
    return "".join(deque(io_, maxlen=n))


if __name__ == "__main__":
    parser = ArgumentParser(description="display the last part of a file")

    parser.add_argument("file", type=FileType("r"), default="-")
    parser.add_argument(
        "-n",
        metavar="number",
        type=int,
        default=10,
        help="The location is number lines.\n"
        "The default starting location is ``-n 10'', "
        "or the last 10 lines of the input.",
    )

    args = parser.parse_args()
    result = tail(args.file, n=args.n)
    stdout.write(result)
