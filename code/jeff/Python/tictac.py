import os

# Game board class
class Board:
    def __init__(self, board, bformat):
        self.board = board
        
    # Board Update method. This updates the location on the board
    def update_board(l: dict , key, value):
        l.update({key: value})
        return l

    def refresh_screen():
        os.system('cls')

def main():
    # Board dictionary
    true_board = {
        "a": ' ',
        "b": ' ',
        "c": ' ',
        "d": ' ',
        "e": ' ',
        "f": ' ',
        "g": ' ',
        "h": ' ',
        "i": ' '
        }
    
    while True:

        fboard ='''
        {a} | {b} | {c}
        {d} | {e} | {f}
        {g} | {h} | {i}
        '''.format(**true_board)

        print(fboard)

        # All possible selections
        accept_char = ['a','b','c','d','e','f','g','h','i']
        

        # User inputs the key value
        value = input('select a key ')

        # For loop to check if the Value is equal to 
        for char in accept_char:
            if value == char:
                Board.update_board(true_board, value,'x')
        

        # The game board format
        Board.refresh_screen()
        
     

main()