from pathlib import Path


def tr(old: str, new: str, filename: str) -> str:
    with open(filename, "r") as f:
        lines = map(lambda line: line.replace(old, new), f.readlines())
        return "".join(lines)


if __name__ == "__main__":
    filename = str((Path(__file__) / "../../hightemp.txt").resolve())
    print(tr("\t", " ", filename))
