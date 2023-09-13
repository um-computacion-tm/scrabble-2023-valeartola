class Player:
    def __init__(self, bag_tiles):
        self.tile = bag_tiles.take(7)
        
    def rellenar(self):
        self.tiles += bag_tiles.take(
            7 - len(self.tiles)
        )