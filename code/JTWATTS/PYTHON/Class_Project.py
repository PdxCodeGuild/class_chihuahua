import random



class Player:
    def __init__(self,name,token):
        self.name= name
        self.token = token
player_1 = Player('alex', 'x')
player_2 = Player('isabel', 'o')



class game:
    def __repr__(self, board):
        self.board = board
            
    def board(self):
        board = {0: ' | ', 1: ' | ', 2: ' | ',
         3: ' | ', 4: ' | ', 5: ' | ',
         6: ' | ', 7: ' | ', 8: ' | '}


    def game_board(board):
        print(board[0] + board[1] + board[2])
        print(board[3] + board[4] + board[5])
        print(board[6] + board[7] + board[8])

    (game_board(board))

    def move(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
    
    def calc_winner(board,letter):
        (board[0] == letter and board[1] == letter and board[2] == letter)
        (board[3] == letter and board[4] == letter and board[5] == letter)
        (board[6] == letter and board[7] == letter and board[8] == letter)
        (board[0] == letter and board[4] == letter and board[7] == letter)
        (board[1] == letter and board[4] == letter and board[7] == letter)
        (board[2] == letter and board[5] == letter and board[8] == letter)
        (board[1] == letter and board[4] == letter and board[7] == letter)
            
    #def is_full():
    
    #def is_game_over():
   
def main():

