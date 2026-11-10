import random

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

moves = []

"""Checking for legal moves and handling the exceptions that can be raised"""
def move_query():
    while True:
        try:
            player_move = int(input("Your move: "))
            if player_move >= 1 and player_move <= 9:
                if player_move not in moves[:][[1]]:
                    moves.append(('O', player_move))
                    break
                raise IndexError # Move is already occupied
            raise IndexError # Out of the bounds of the list
        
        except ValueError:
            print("Please enter correct move")
            continue
        except IndexError:
            print("Please play a legal move")
            continue
        except:
            print("Some system failure might have happened. Please try again")
            continue

"""Making move"""
def make_move():
    for row in range(3):
        for col in range(3):
            board[row][col] = moves[:][0]
    pass

"""Generating random move"""
def generate_move():
    possible = False
    while not possible:
        bot_move = random.randint(1, 9)
        if bot_move not in moves[:][1]:
            moves.append(('X', bot_move))
            break

board = [[j * 3 + i + 1 for i in range(3)] for j in range(3)]

board_maker(board)
