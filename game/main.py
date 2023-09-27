from game.scrabble import ScrabbleGame

def main():
    while True:
        try:
            players_count = int(input('ingrese cantidad de jugadores: '))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("valor invalido")