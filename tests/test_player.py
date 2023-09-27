import unittest
from game.player import Player
from game.models import Tile

class TestPayer(unittest.TestCase):
    def tesst_init(self):
        player_1 = Player() #player_1 (objeto) Player(clase)
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
"""   def test_validate_user_has_letters(self):
        tiles = [
            Tile(letter="H", value=1),
            Tile(letter="O", value=1),
            Tile(letter="L", value=1),
            Tile(letter="A", value=1),
        ]
        """

if __name__ == "__main__":
    unittest.main()