from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, "") for _ in range(15)]
            for _ in range(15)
        ]
    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        pos_x = location[0] 
        pos_y = location[1]

        if orientation == "H":
            if pos_x + len_word > 15:
                return False
            else:
                return True
        elif orientation == "V":
            if pos_y + len_word > 15:
                return False
            else:
                return True
    
"""    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )"""