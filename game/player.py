from game.models import BagTiles

class Player:
    def __init__(self, id:int):
        self.id = id
        bag = BagTiles()
        self.tiles = bag.take(7)
        self.score = 0


    # def set_name(self, name = None):
    #     self.name = name
    #     return name
    
    def has_letters(self, tiles):
        player_bag = self.tiles
        for tile in tiles:
            if tile.letter not in player_bag:
                return False
            else:
                return True
        
    # def refill(self, bag):
    #     needed_tiles = 7 - len(self.tiles)
    #     if needed_tiles > 0:
    #         new_tiles = bag.take(needed_tiles)
    #         self.tiles += new_tiles
