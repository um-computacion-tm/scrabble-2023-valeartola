from game.scrabble import ScrabbleGame

def main():
    print("BIENVENIDO!")

    while True:
        try:
            players_count = int(input ("Ingrese cantidad de jugadores:  "))
            if players_count <=1  or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")

    scrabble_game = ScrabbleGame(players_count = players_count)
    print("Cantidad de jugadores: ", len (scrabble_game.players))
    scrabble_game.next_turn()
    print(f"Turno del jugador "())

    while True:
        word = input("Ingrese una palabra: ")
        location = input("Ingrese la ubicación (fila, columna): " ) 
        orientation = input("Ingrese la orientación (H para horizontal, V para vertical): ")

        if scrabble_game.board.validate_word_inside_board(word, location, orientation):
            print(f"Turno del jugador {players_count}")
        else:
            print("Palabra no válida. Inténtalo de nuevo.")
