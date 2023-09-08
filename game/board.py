from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, "") for _ in range(15)]
            for _ in range(15)
        ]
    def validate_word_inside_board(self, word, location, orientation):
        longitud_word = len(word)
        fila, columna = location
        if orientation == "H":
            if columna + longitud_word <=15:
                if i in range(longitud_word):
                    if self.grid[fila][columna + i]. esta_vacia():
                        return True
            return False
        elif orientation == "V":
            if fila + longitud_word <= 15:
                # Verificar si cada celda que ocuparía la palabra está vacía
                for i in range(longitud_word):
                    if self.grid[fila + i][columna].esta_vacia():
                        return True
            return False
        else:
            return False

