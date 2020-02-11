import unittest
from contextlib import ExitStack
from pathlib import Path
import subprocess
from src.ch2._13.paste import paste


class TestPaste(unittest.TestCase):
    def test_paste(self):
        result = paste(["a", "b", "c"], ["1", "2", "3"])

        self.assertEqual(result, ("a\t1\n" "b\t2\n" "c\t3\n"))

    def test_paste_space_delimiter(self):
        result = paste(["a", "b", "c"], ["1", "2", "3"], delimiter=" ")

        self.assertEqual(result, ("a 1\n" "b 2\n" "c 3\n"))

    def test_paste_with_command(self):
        workdir = Path(__file__).parent
        with ExitStack() as stack:
            filepaths = list(map(lambda i: str((workdir / f"../../../src/ch2/_12/col{i}.txt").resolve()), [1, 2],))

            col1, col2 = map(lambda filepath: stack.enter_context(open(filepath, "r")), filepaths)

            expected = subprocess.check_output(f"paste {' '.join(filepaths)}", shell=True).decode()

            self.assertEqual(paste(col1, col2), expected)


if __name__ == "__main__":
    unittest.main()
