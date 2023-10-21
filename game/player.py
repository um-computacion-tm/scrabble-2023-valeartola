from game.models import BagTiles

class Player:
    # def __init__(self, id:int):
    #     self.id = id
    #     bag = BagTiles()
    #     self.tiles = bag.take(7)
    #     self.score = 0


    # def set_name(self, name = None):
    #     self.name = name

    # def get_name(self):
    #     return self.name
    
    
    # def has_letters(self, tiles):
    #     player_bag = self.tiles
    #     for tile in tiles:
    #         if tile.letter not in player_bag:
    #             return False
    #         else:
    #             return True
        
    # # def refill(self, bag):
    # #     needed_tiles = 7 - len(self.tiles)
    # #     if needed_tiles > 0:
    # #         new_tiles = bag.take(needed_tiles)
    # #         self.tiles += new_tiles

def __init__(self):
        self.name = ""
        self.tiles = []
        self.score = 0

    def set_name(self,name):
        self.name = name
    
    def get_name(self):
        return self.name

    def take_tiles(self, bag:BagTiles, amount):
        self.tiles.extend(bag.take(amount))
    
    def increase_score(self,amount):
        self.score += amount

    def get_score(self):
        return self.score

    def refill(self,bag:BagTiles):
        self.tiles += bag.take(
            7- len(self.tiles)
        )

    def has_letters(self, tiles=[]):
        letras_jugador = [tile.letter for tile in self.tiles]
        letras_palabra = [tile.letter for tile in tiles]
        letras_necesarias = Counter(letras_palabra)
        for letra, cantidad in letras_necesarias.items():
            if letras_jugador.count(letra) < cantidad:
                return False
        return True