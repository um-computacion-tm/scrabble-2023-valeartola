import unittest
from Game.player import Player

class TestPayer(unittest.TestCase):
    def tesst_init(self):
        player_1 = Player() #player_1 (objeto) Player(clase)
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

if __name__ == "__main__":
    unittest.main()