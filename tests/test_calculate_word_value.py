import unittest
from Game.models import Tile
from Game.cell import Cell
from .... import calculate_word_value

class TestsCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter=Tile("C", 1)),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2)),
            Cell(letter=Tile"A", 1)
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_letter_with_multiplier(self):
        word = [
            Cell(letter=Tile("C", 1)),
            Cell(letter=Tile("A", 1)),
            Cell(
                letter=Tile("S", 2),
                multiplier=2,
                multiplier_type="letter"),
            Cell(letter=Tile"A", 1)
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 10)
    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)




if __name__ == "__main__":
    unittest.main()