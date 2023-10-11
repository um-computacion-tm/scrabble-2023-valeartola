import unittest
from game.models import Tile
from game.cell import Cell


class TestsCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        cell = Cell(multiplier=None, multiplier_type="")
        word = [
            Cell(letter=Tile("C", 1, 4)),
            Cell(letter=Tile("A", 1, 12)),
            Cell(letter=Tile("S", 2, 6)),
            Cell(letter=Tile("A", 1, 12))
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_letter_with_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type="")
        word = [
            Cell(letter=Tile("C", 1, 4)),
            Cell(letter=Tile("A", 1, 12)),
            Cell(
                letter=Tile("S", 2, 6),
                multiplier=2,
                multiplier_type="letter"),
            Cell(letter=Tile("A", 1, 12))
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type="")
        word = [
            Cell(letter=Tile('C', 1, 4)),
            Cell(letter=Tile('A', 1, 12)),
            Cell(
                letter=Tile('S', 2, 6),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1, 12)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 10)
    def test_with_letter_word_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type="")
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1, 4)
            ),
            Cell(letter=Tile('A', 1, 12)),
            Cell(
                letter=Tile('S', 2, 6),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1, 12)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        cell = Cell(multiplier=None, multiplier_type="")
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1, 4)
            ),
            Cell(letter=Tile('A', 1, 12)),
            Cell(
                letter=Tile('S', 2, 6),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1, 12)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_empty_word(self):
        cell = Cell(multiplier=None, multiplier_type="")
        word = []  # Word vacío
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 0)




if __name__ == "__main__":
    unittest.main()