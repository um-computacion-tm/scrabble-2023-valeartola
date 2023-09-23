from game.models import Tile

class Cell:
    def __init__(self, multiplier=1, multiplier_type="", letter = None, word=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.word = word
        self.active = True
    
    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == "letter":
            value = self.letter.value * self.multiplier
            self.multiplier_type = None
            return value
        else:
            return self.letter.value
        
        
"""    def calculate_word_value(self):
        word_value = 0
        word_multiplier = 1
        for letter in word:
            word_value += letter.calculate_value()
            if letter.multiplier_type == 'word':
                word_multiplier = letter.multiplier
                letter.multiplier_type = None
        word_value *= word_multiplier
        return word_value"""

def calculate_word_value(self):
    if self.word is None:
        return 0
    
    word_value = 0
    word_multiplier = 1
    
    for letter in self.word.cells:
        word_value += letter.calculate_value()
        if letter.multiplier_type == 'word':
            word_multiplier *= letter.multiplier
            letter.multiplier_type = None
    
    word_value *= word_multiplier
    return word_value

    
    