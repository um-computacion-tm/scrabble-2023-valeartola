import unittest
from Game.models import (Tile, BagTiles)

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile("A", 1)
        self.assertEqual(tile.letter, "A")
        self.assertEqual(tile.value, 1)

class TestBagTile(unittest.TestCase):
    def test_bag_tiles(self):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            5,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
        3)
        self.assertEqual(
            len(tiles),
        2)

    def test_put(self):
        bag = BagTiles()
        put_tiles =(Tile("Z", 1), Tile("Y",1))
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
        7)
if __name__ == "__main__":
    unittest.main()