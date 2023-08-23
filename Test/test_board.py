import unittest
from Game.board import Board

class TestPayer(unittest.TestCase):
    def tesst_init(self):
        grid = Board() #player_1 (objeto) Player(clase)
        self.assertEqual(
            len(board.grid.tiles),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
        

if __name__ == "__main__":
    unittest.main()