from game.cell import Cell

triple_word = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
double_word = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
triple_letter = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
double_letter = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))



class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, "") for _ in range(15)]
            for _ in range(15)
        ]
        self.add_special_cells()
        
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
    
    def cell_multiplier(self,ubication, multiplier_type_cell, multiplier_value_cell):
        cell = self.grid[ubication[0]][ubication[1]]
        cell.multiplier_type_cell = multiplier_type_cell
        cell.multiplier = multiplier_value_cell

    def add_special_cells(self):
        for ubication in triple_word:
            self.cell_multiplier(ubication, "word", 3)
        for ubication in double_word:
            self.cell_multiplier(ubication, "word", 2)
        for ubication in triple_letter:
            self.cell_multiplier(ubication, "letter", 3)
        for ubication in double_letter:
            self.cell_multiplier(ubication, "letter", 2)

    def put_words(self, word, location, orientation):
        len_word = len(word)
        pos_x = location[0]
        pos_y = location[1]
        if orientation == 'H':
            for i in range (len_word):
                self.grid[pos_x][pos_y + i].add_letter(word[i])
        else:
            for i in range (len_word):
                self.grid[pos_x + i][pos_y].add_letter(word[i])

    def validate_word_place_board(self,word,location,orientation):
        center_of_board = (7, 7)
        for i in range(len(word)):
            pos_x = location[0] + i if orientation == "H" else location[0] 
            pos_y = location[1] + i if orientation == "V" else location[1] 
            print(f"posicion ({pos_x}, {pos_y}) de letra '{word[i]}'")
            if pos_x == center_of_board[0] and pos_y == center_of_board[1]: 
                print ("pasa por el centro")
                return True
        return False


    # def show_board(board):
    #     print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
    #     for row_index, row in enumerate(board.grid):
    #         print(
    #             str(row_index).rjust(2) +
    #             '| ' +
    #             ' '.join([repr(cell) for cell in row])
    #         )