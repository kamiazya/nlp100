import unittest
from pathlib import Path
import subprocess
from src.ch2._11.tr import tr


class TestTr(unittest.TestCase):
    def test_tr(self):
        filename = str((Path(__file__) / "../../../../src/ch2/hightemp.txt").resolve())
        result = tr("\t", " ", filename)
        command = f"cat {filename} | tr '\\t' ' '"
        check_tr = subprocess.check_output(command, shell=True)
        self.assertEqual(result, check_tr.decode())


if __name__ == "__main__":
    unittest.main()
