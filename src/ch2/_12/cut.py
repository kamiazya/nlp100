from pathlib import Path
from typing import Optional, List


def cut(filename: str, *, f: int, d: Optional[str] = "\t") -> str:
    with open(filename, "r") as file:
        lines: List[str] = file.readlines()
        return "\n".join(map(lambda l: l.rstrip().split(d)[f-1], lines)) + "\n"


if __name__ == "__main__":
    filename = str((Path(__file__) / "../../hightemp.txt").resolve())

    workdir = Path(__file__).parent

    for i in [1, 2]:
        with open(str((workdir / f"col{i}.txt").resolve()), "w") as output:
            output.write(cut(filename, f=i))
