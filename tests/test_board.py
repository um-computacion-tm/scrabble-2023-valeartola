import unittest
from game.board import Board

class TestPayer(unittest.TestCase):
    def tesst_init(self):
        board = Board() #player_1 (objeto) Player(clase)
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location =(5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True 

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False

if __name__ == "__main__":
    unittest.main()