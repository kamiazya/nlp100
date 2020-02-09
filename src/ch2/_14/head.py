from sys import stdout
from typing import IO
from itertools import islice
from argparse import ArgumentParser, FileType


def head(io_: IO[str], *, n: int = 1) -> str:
    return "".join(islice(io_, n))


if __name__ == "__main__":
    parser = ArgumentParser(
        description="display first lines of a file")

    parser.add_argument("file",
                        type=FileType("r"),
                        default="-")
    parser.add_argument("-n",
                        metavar="count",
                        type=int,
                        help="If count is omitted it defaults to 10.",
                        default=10)

    args = parser.parse_args()
    result = head(args.file, n=args.n)
    stdout.write(result)
