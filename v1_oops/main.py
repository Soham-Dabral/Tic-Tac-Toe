player_x = 'X'
player_o = 'O'

class Game():
    def __init__(self, max_size: int = 3):
        self.player_x = player_x
        self.player_o = player_o
        self.current_player = self.player_x
        
        self.board = [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']
        ]

        self.max_size = max_size

    def display_board(self):
        for row in self.board:
            print(row)

    def get_move(self):
        while True:
            try:
                print(f"Player {self.current_player}'s Turn")
                row = int(input("Row: "))
                column = int(input("Column: "))
                            
            except ValueError:
                print("Enter integers only")
                continue

            if not (0 <= row <= self.max_size and 0 <= column <= self.max_size):
                print("Coordinates are out of range")
                continue

            if  self.board[row][column] != '.':
                print("Position already occupied")
                continue
        
            return (row, column)
    
    def place_move(self, row, column, current_player):
        self.board[row][column] = current_player
        return self.board
    
    def check_winner(self, current_player):
        #Rows
        for row in self.board:
            if row == [current_player, current_player, current_player]:
                return True
        
        #Column
        for column in range(self.max_size):
            if self.board[0][column] == current_player and self.board[1][column] == current_player and self.board[2][column] == current_player:
                return True
        
        left_diagonal = []
        right_diagonal = []
        
        #Diagonals
        for i in range(self.max_size):
            left_diagonal.append(self.board[i][i])
            right_diagonal.append(self.board[self.max_size - 1 - i][i])
            
        if left_diagonal == [current_player, current_player, current_player]:
            return True

        if right_diagonal == [current_player, current_player, current_player]:
            return True
    
        return False

    def check_draw(self):
        counter = 0
        for row in self.board:
            if '.' not in row:
                counter += 1
                if counter == 3:
                    return True
        
        return False
    
    def switch_player(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        
        else:
            self.current_player = self.player_x
    
    def run(self):
        while True:
            self.display_board()
            
            row, column = self.get_move()

            self.place_move(row, column, self.current_player)

            if self.check_winner(self.current_player):
                self.display_board()
                print(f"The Winner is {self.current_player}")
                return

            if self.check_draw():
                self.display_board()
                print(f"Very tough game, but the game is Draw")
                return
            
            self.switch_player()

game = Game()
game.run()

            
