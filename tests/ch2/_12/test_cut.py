import unittest
from pathlib import Path
import subprocess
from src.ch2._12.cut import cut


class TestCut(unittest.TestCase):

    def test_cut(self):
        for i in range(1, 5):
            filename = str(
                (Path(__file__) / "../../../../src/ch2/hightemp.txt").resolve()
            )
            result = cut(filename, f=i)
            command = f"cut -f {i} {filename}"
            check_cut = subprocess.check_output(command, shell=True)
            self.assertEqual(result, check_cut.decode())


if __name__ == "__main__":
    unittest.main()
