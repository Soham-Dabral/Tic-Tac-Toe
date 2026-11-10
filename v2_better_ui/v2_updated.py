import random


human = False # Play with Human
bot = True # Play with Bot

# game_mode = input("Choose a game mode b/h: ").lower().strip()

"""Creation of the outline of the board"""
def board_maker(board):
    print('+-------' * 3, '+', sep="")
    for row in range(3):
        print('|       ' * 3, '|', sep="")
        for col in range(3):
            print('|   ' + str(board[row][col]) + '   ', end="")
        print('|')
        print('|       ' * 3, '|', sep="")
        print('+-------' * 3, '+', sep="")




board = [[j * 3 + i + 1 for i in range(3)] for j in range(3)]
# print(board)
board_maker(board)

moves = []
