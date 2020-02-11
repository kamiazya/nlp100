import unittest

from src.ch1._04.atoms import main


class TestAtoms(unittest.TestCase):
    def test_main(self):
        self.assertEqual(
            main(),
            [
                "H",
                "He",
                "Li",
                "Be",
                "B",
                "C",
                "N",
                "O",
                "F",
                "Ne",
                "Na",
                "Mi",
                "Al",
                "Si",
                "P",
                "S",
                "Cl",
                "Ar",
                "K",
                "Ca",
            ],
        )


if __name__ == "__main__":
    unittest.main()
