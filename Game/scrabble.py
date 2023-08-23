from Game.board import Board
from Game.models import BagTiles
from Game.player import Player

class ScrabbleGame:
    def __init__(self, player_count):
        self.board = Board()
        self.tile_bag = BagTiles()
        for _in range(player_count):
            self.player.append(Player())