import unittest
from src.ch1._07.function import func


class TestFunction(unittest.TestCase):
    def test_func(self):
        cases = [
            {"x": 12, "y": "気温", "z": 22.4, "result": "12時の気温は22.4"},
            {"x": 23, "y": "湿度", "z": 50.0, "result": "23時の湿度は50.0"},
        ]

        for case in cases:
            self.assertEqual(func(case["x"], case["y"], case["z"]), case["result"])


if __name__ == "__main__":
    unittest.main()
