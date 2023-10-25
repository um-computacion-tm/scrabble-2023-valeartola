from game.models import BagTiles
from collections import Counter

class Player:

        def __init__(self):
            self.name = ""
            self.tiles = []
            self.score = 0

        def set_name(self,name):
            self.name = name
        
        def get_name(self):
            return self.name
        
        def increase_score(self,amount):
            self.score += amount

        def get_score(self):
            return self.score
        
        def show_tiles(self):
            return self.tiles        

        def take_tiles(self, bag:BagTiles, amount):
            self.tiles.extend(bag.take(amount))
        
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
        
        def draw_tiles(self, bag, num_tiles):
            if num_tiles <= len(bag.tiles):
                self.tiles.extend(bag.tiles[:num_tiles])
                del bag.tiles[:num_tiles]