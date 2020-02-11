import unittest
from pathlib import Path
import subprocess
from src.ch2._10.wc_l import wc_l


class TestWcL(unittest.TestCase):
    def test_wc_l(self):
        filename = str((Path(__file__) / "../../../../src/ch2/hightemp.txt").resolve())
        result = wc_l(filename)
        command = f"cat {filename} | wc -l | awk " + "'{print $1}'"
        check_wc = subprocess.check_output(command, shell=True)
        self.assertEqual(result, int(check_wc))


if __name__ == "__main__":
    unittest.main()
