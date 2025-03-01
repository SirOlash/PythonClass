from board import Board
from cell import Cell


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.player1_symbol = Cell.X
        self.player2_symbol = Cell.O
        self.current_symbol = self.player1_symbol

    def switch_player(self):
        if self.current_symbol == self.player1_symbol:
            self.current_symbol = self.player2_symbol
        else:
            self.current_symbol = self.player1_symbol

    def player_movement(self,row,col):
        if self.board.set_cell(row, col, self.current_symbol):
            winner = self.board.check_winner()
            if winner:
                self.board.print_board()
                print(f"Congratulations! The player with {self.current_symbol.value} wins!")
                return True

            elif self.board.is_full():
                self.board.print_board()
                print('Its a draw')
                return True
            else:
                self.switch_player()
                return False
        else:
            print("This cell is already occupied, choose another one.")
            return False

    def lets_play(self):
        print("Welcome to Tic-Tac-Toe! \nPlayer 1 is X and Player 2 is O.")
        print("")
        while True:
            self.board.print_board()
            print(f"Current turn: {self.current_symbol.value}")
            try:
                cell_number = int(input("Enter a cell number (1-9): "))
                if cell_number not in range(1, 10):
                    print("Please choose a number between 1 and 9.")
                    continue
                row = (cell_number - 1) // 3
                col = (cell_number - 1) % 3
            except ValueError:
                print("Invalid input. Please enter an integer from 1 to 9.")
                continue

            if self.player_movement(row, col):
                break
if __name__ == "__main__":
    game = TicTacToe()
    game.lets_play()

