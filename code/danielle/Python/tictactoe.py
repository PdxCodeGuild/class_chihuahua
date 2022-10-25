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
    
    def check_win_x(l: dict):
        if l['a'] == 'x' and l['b'] == 'x' and l['c'] == 'x':
            status = 1
            print('win')
            return status
        elif l['d'] == 'x' and l['e'] == 'x' and l['f'] == 'x':
            status = 1
            print('win')
            return status
        elif l['g'] == 'x' and l['h'] == 'x' and l['i'] == 'x':
            status = 1
            print('win')
            return status
        elif l['a'] == 'x' and l['d'] == 'x' and l['g'] == 'x':
            status = 1
            print('win')
            return status
        elif l['h'] == 'x' and l['e'] == 'x' and l['b'] == 'x':
            status = 1
            print('win')
            return status
        elif l['c'] == 'x' and l['f'] == 'x' and l['i'] == 'x':
            status = 1
            print('win')
            return status
        elif l['a'] == 'x' and l['e'] == 'x' and l['i'] == 'x':
            status = 1
            print('win')
            return status
        elif l['g'] == 'x' and l['e'] == 'x' and l['c'] == 'x':
            status = 1
            print('win')
            return status
        else:
            status = 2
            return status

    def check_win_o(l: dict):
        if l['a'] == 'o' and l['b'] == 'o' and l['c'] == 'o':
            status = 1
            print('win')
            return status
        elif l['d'] == 'o' and l['e'] == 'o' and l['f'] == 'o':
            status = 1
            print('win')
            return status
        elif l['g'] == 'o' and l['h'] == 'o' and l['i'] == 'o':
            status = 1
            print('win')
            return status
        elif l['a'] == 'o' and l['d'] == 'o' and l['g'] == 'o':
            status = 1
            print('win')
            return status
        elif l['b'] == 'o' and l['e'] == 'o' and l['h'] == 'o':
            status = 1
            print('win')
            return status
        elif l['c'] == 'o' and l['f'] == 'o' and l['i'] == 'o':
            status = 1
            print('win')
            return status
        elif l['c'] == 'o' and l['e'] == 'o' and l['g'] == 'o':
            status = 1
            print('win')
            return status
        elif l['a'] == 'o' and l['e'] == 'o' and l['i'] == 'o':
            status = 1
            print('win')
            return status
        else:
            status = 2
            return status 

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def player_name(self):
        return self.name
    
    def player_marker(self):
        return self.marker
    
def main():
    player_1 = Player('Bob', 'x') 
    player_2 = Player('Steve', 'o')

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
        ---------
        {d} | {e} | {f}
        ---------
        {g} | {h} | {i}
        '''.format(**true_board)

        print(fboard)
        # All possible selections
        accept_char = ['a','b','c','d','e','f','g','h','i']
        

        # Player 1 inputs the key value
        p_value = input(' Player 1 select a key ')
        # For loop to check if the Value is equal to

        for char in accept_char:
            if p_value == char:
                Board.update_board(true_board, p_value, Player.player_marker(player_1))
        
        if Board.check_win_x(true_board) == 1:
            Board.refresh_screen()
            fboard ='''
            {a} | {b} | {c}
            ---------
            {d} | {e} | {f}
            ---------
            {g} | {h} | {i}
            '''.format(**true_board)
            print(fboard)
            print(f'{Player.player_name(player_1)} Is the winner!')    
            break
        
        Board.refresh_screen()

        fboard ='''
        {a} | {b} | {c}
        ---------
        {d} | {e} | {f}
        ---------
        {g} | {h} | {i}
        '''.format(**true_board)
        print(fboard)

        # User inputs the key value
        c_value = input(' Player 2 select a key ')

        # For loop to check if the Value is equal to

        for char in accept_char:
            if p_value == char:
                Board.update_board(true_board, c_value, Player.player_marker(player_2))
        
        if Board.check_win_o(true_board) == 1:
            Board.refresh_screen()
            fboard ='''
            {a} | {b} | {c}
            ---------
            {d} | {e} | {f}
            ---------
            {g} | {h} | {i}
            '''.format(**true_board)
            print(fboard)
            print(f'{Player.player_name(player_2)} Is the winner!')
            break
    
        # The game board format
        Board.refresh_screen()
        
main()