import random

board = [[j * 3 + i + 1 for i in range(3)] for j in range(3)]

"""Dictionary to store the coordinates"""
coordinates = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0), "8": (2, 1), "9": (2, 2)}


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

# A list of tuples that contains (symbol, position)
moves = []

"""Checking for legal moves and handling the exceptions that can be raised"""
def move_query(moves):
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

"""Generating random move"""
def generate_move():
    # Check all the available moves where the bot can play
    available = [i for i in range(1, 10) if i not in [move[1] for move in moves]]
    if available:
        bot_move = random.choice(available) # Generating the computer's move
        moves.append(('X', bot_move))

"""Checking for victory"""
def check_win(board, sign):
    if sign == 'O':
        winner = 'you'
    elif sign == 'X':
        winner = 'pc'
    else:
        winner = None

    # Winning cases
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return winner
        if all(board[j][i] == sign for j in range(3)):
            return winner
        if all(board[j][j] == sign for j in range(3)): #board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return winner
        if all(board[j][2 - j] == sign for j in range(3)):
            return winner
        else:
            return None

"""Updating the board"""
def update_board(board):
    for symbol, value in moves:
        row, col = coordinates[str(value)]
        board[row][col] = symbol
    return 

game_over = False
board_maker(board)

board[1][1] = 'X'
while (len(moves) < 9 or game_over):
    
    move_query(moves) # Ask for a move
    if check_win(board, 'O'):
        game_over = True
        print('You won!')
        break

    generate_move() # Generate bot's move
    if check_win(board, 'X'):
          game_over = True
          print('You lost!')
          break

    update_board(board) # Update tge board
    board_maker(board) # Draw the updated board
