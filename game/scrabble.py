from game.board import Board
from game.models import BagTiles
from game.player import Player

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(self.bag_tiles))
        self.current_player = None

    def playing(self):
        return True



    def get_player_count(self):
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
               print('ingrese un numero por favor')
        return player_count


    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player)
            if index == len(self.players) - 1:
               self.current_player = self.players[0]
            else:
                self.current_player = self.players[index + 1]

    # def play(self, word, location, orientation):
    #     self.validate_word(word, location, orientation)
    #     words = self.board.put_words(word, location, orientation)
    #     total = self.cell.calculate_word_value(words)
    #     self.players[self.current_player].score += total
    #     self.next_turn()

