# board ={0: '1', 1: '|', 2: '2',
#         3: '|', 4: '3', 5: '4',
#         6: '|', 7: '5', 8: '|', 
#         9: '6', 10: '7', 11: '|', 
#         12: '8', 13: '|', 14: '9'}
        
# game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"
# list_game_board = [board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9], board[10], board[11], board[12], board[13], board[14]]
# print(game_board)

# count = 0
# player_1_turns = set()
# options = {'1': board[0], '2': board[2], '3': board[4], '4': 
# board[5], '5': board[7], '6': board[9], '7': board[10], '8': board[12], '9': board[14]}

# while True:
#     if count < 5:
#         ask_user = input("Please choose a place on the board (1-9): ")
#         player_1_turns.add(options[ask_user])

#         # new_board = list(board)
#         # print(new_board)
#         # board_list = list(board.items())
#         # board_list[int(ask_user)] = (int(ask_user), 'X')
#         # print(board_list)
#         # del board[int(ask_user)]
#         new_value = {int(ask_user): 'X'}
#         # board.update({int(ask_user): 'X'})
#         # print(game_board)
#         # new_board = board
#         for key in board:
#             if key in new_value:
#                 board[key] = new_value[key]
#                 game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"
#         #         del options[ask_user]
            
#         count += 1

#     print(board)
#     print(game_board)
#     print(options)
#     print(player_1_turns)


    #********************************************************************************************************************************************

# board ={0: '0', 1: '|', 2: '1',
#     3: '|', 4: '2', 5: '3',
#     6: '|', 7: '4', 8: '|', 
#     9: '5', 10: '6', 11: '|', 
#     12: '7', 13: '|', 14: '8'}
        
# game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"

# print(game_board)

# count = 0
# player_1_turns = set()
# options = {0: board[0], 1: board[2], 2: board[4], 3: 
# board[5], 4: board[7], 5: board[9], 6: board[10], 7: board[12], 8: board[14]}

# while True:
#     if count < 5:
#         ask_user_str = input("Please choose a place on the board (1-9): ")
#         ask_user = int(ask_user_str)
#         if ask_user == 0:
#             ask_user += 0
#         elif ask_user == 1:
#             ask_user += 1
#         elif ask_user > 1 and ask_user < 4:
#             ask_user += 2
#         elif ask_user == 4:
#             ask_user += 3
#         else:
#             ask_user += 4
#         player_1_turns.add(options[ask_user])
#         new_value = {int(ask_user): 'X'}
#         for key in board:
#             if key in new_value:
#                 board[key] = new_value[key]
#                 game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"
#                 del options[ask_user]
            
#         count += 1

#     print(board)
#     print(game_board)
#     print(options)
#     print(player_1_turns)

    #**************************************************************************************************************************

# class Player:
#     def __init__(self, name, token):
#         self.name = name
#         self.token = token

#         pass   
# board ={0: '0', 1: '|', 2: '1',
#     3: '|', 4: '2', 5: '3',
#     6: '|', 7: '4', 8: '|', 
#     9: '5', 10: '6', 11: '|', 
#     12: '7', 13: '|', 14: '8'}
        
# game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"

# print(game_board)

# count = 0
# player_1_turns = set()
# options = {0: board[0], 1: board[2], 2: board[4], 3: 
# board[5], 4: board[7], 5: board[9], 6: board[10], 7: board[12], 8: board[14]}

# while True:
#     if count <= 4:
#         ask_user_str = input("Please choose a place on the board (0-8): ")
#         ask_user = int(ask_user_str)
#         player_1_turns.add(options[ask_user])
#         if ask_user == 0:
#             ask_user += 0
#         elif ask_user == 1:
#             ask_user += 1
#         elif ask_user == 2:
#             ask_user += 2
#         elif ask_user == 3:
#             ask_user += 2
#         elif ask_user == 4:
#             ask_user += 3
#         elif ask_user == 5:
#             ask_user += 4
#         elif ask_user == 6:
#             ask_user += 4
#         elif ask_user == 7:
#             ask_user += 5
#         else:
#             ask_user += 6
#         new_value = {(ask_user): 'X'}
#         for key in board:
#             if key in new_value:
#                 board[key] = new_value[key]
#                 game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"
#                 del options[int(ask_user_str)]
            
#         count += 1

#     elif count >= 5:    

#         win_horizontal_1 = {0, 2, 4}
#         win_horizontal_2 = {5, 7, 9}
#         win_horizontal_3 = {10, 12, 14}
#         win_vert_1 = {0, 5, 10}
#         win_vert_2 = {2, 7, 12}
#         win_vert_3 = {4, 9, 14}

#         if win_horizontal_1.intersection(player_1_turns) == player_1_turns:
#             print("You won")
#             print(win_horizontal_1.intersection(player_1_turns))
#         break

#     print(board)
#     print(game_board)
#     print(options)
#     print(player_1_turns)

    #******************************************************************************************************************




class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        
class Game(Player):
    def __init__(self, name, token, board):
        self.board = board



        # board ={0: '0', 1: '|', 2: '1',
        #     3: '|', 4: '2', 5: '3',
        #     6: '|', 7: '4', 8: '|', 
        #     9: '5', 10: '6', 11: '|', 
        #     12: '7', 13: '|', 14: '8'}
            
        # return board

    def nice_board(board):
        game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"
        print(game_board)
        return game_board


    def play(board, options):

        options = {0: board[0], 1: board[2], 2: board[4], 3: 
        board[5], 4: board[7], 5: board[9], 6: board[10], 7: board[12], 8: board[14]}
        return options

    def moves(options, board):

        while True:
            count = 0
            player_1_turns = set()
            if count <= 4:
                ask_user_str = input("Please choose a place on the board (0-8): ")
                ask_user = int(ask_user_str)
                player_1_turns.add(options[ask_user])
                if ask_user == 0:
                    ask_user += 0
                elif ask_user == 1:
                    ask_user += 1
                elif ask_user == 2:
                    ask_user += 2
                elif ask_user == 3:
                    ask_user += 2
                elif ask_user == 4:
                    ask_user += 3
                elif ask_user == 5:
                    ask_user += 4
                elif ask_user == 6:
                    ask_user += 4
                elif ask_user == 7:
                    ask_user += 5
                else:
                    ask_user += 6
                new_value = {(ask_user): 'X'}
                for key in board:
                    if key in new_value:
                        board[key] = new_value[key]
                        game_board = f"{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}\n{board[5]}{board[6]}{board[7]}{board[8]}{board[9]}\n{board[10]}{board[11]}{board[12]}{board[13]}{board[14]}"
                        del options[int(ask_user_str)]
                    
                count += 1

            elif count >= 5:    

                win_horizontal_1 = {0, 2, 4}
                win_horizontal_2 = {5, 7, 9}
                win_horizontal_3 = {10, 12, 14}
                win_vert_1 = {0, 5, 10}
                win_vert_2 = {2, 7, 12}
                win_vert_3 = {4, 9, 14}

                if win_horizontal_1.intersection(player_1_turns) == player_1_turns:
                    print("You won")
                    print(win_horizontal_1.intersection(player_1_turns))
                break
board ={0: '0', 1: '|', 2: '1',
            3: '|', 4: '2', 5: '3',
            6: '|', 7: '4', 8: '|', 
            9: '5', 10: '6', 11: '|', 
            12: '7', 13: '|', 14: '8'}
player_1 = Player('namey', 'X')
game = Game(player_1, 'X', board)
print(game)
print(Game.moves)
print(board)
# print(game_board)
# print(options)
# print(player_1_turns)