import string
name = "ayo"
print(name)
print(id(name))
name = "ayoee"
print(name)
print(id(name))
another_name = "ay.omide"
print(another_name)
print(id(another_name))
print(another_name.split("."))



#help(another_name.casefold)

names = ['esther','bimbo','moses']
print("/ ".join(names))

letter = string.ascii_letters
# print((list(letter)))
# print("-".join(letter))
# print(letter.isa) #character testing method


from enum import Enum


# Enum to represent the state of each cell on the board
class Cell(Enum):
    EMPTY = " "
    X = "X"
    O = "O"


# Class to manage the game board
class Board:
    def __init__(self):
        # Create a 3x3 grid filled with EMPTY cells
        self._grid = [[Cell.EMPTY for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self._grid:
            print(" | ".join(cell.value for cell in row))
            print("-" * 9)

    def set_cell(self, row, col, cell: Cell):
        # Only set the cell if it is EMPTY
        if self._grid[row][col] == Cell.EMPTY:
            self._grid[row][col] = cell
            return True
        else:
            return False

    def check_winner(self):
        grid = self._grid
        # Check rows
        for row in grid:
            if row[0] == row[1] == row[2] != Cell.EMPTY:
                return row[0]
        # Check columns
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] != Cell.EMPTY:
                return grid[0][col]
        # Check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] != Cell.EMPTY:
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != Cell.EMPTY:
            return grid[0][2]
        return None

    def is_full(self):
        # Returns True if no cell is EMPTY
        return all(cell != Cell.EMPTY for row in self._grid for cell in row)


# Game controller class for Tic-Tac-Toe
class TicTacToe:
    def __init__(self):
        self.board = Board()
        # Automatically assign symbols: Player 1 is X and Player 2 is O
        self.player1_symbol = Cell.X
        self.player2_symbol = Cell.O
        # Start with Player 1
        self.current_symbol = self.player1_symbol

    def switch_player(self):
        # Switch the current player by alternating between X and O
        self.current_symbol = (
            self.player2_symbol if self.current_symbol == self.player1_symbol else self.player1_symbol
        )

    def play_move(self, row, col):
        # Try to set the cell with the current player's symbol
        if self.board.set_cell(row, col, self.current_symbol):
            winner = self.board.check_winner()
            if winner:
                self.board.print_board()
                print(f"Congratulations! The player with {self.current_symbol.value} wins!")
                return True  # Game over
            elif self.board.is_full():
                self.board.print_board()
                print("It's a draw!")
                return True  # Game over
            else:
                self.switch_player()  # Continue game by switching turn
                return False  # Game continues
        else:
            print("Invalid move! That cell is already occupied. Try again!")
            return False  # Game continues

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Player 1 is X and Player 2 is O. Let the game begin!")
        while True:
            self.board.print_board()
            print(f"Current turn: {self.current_symbol.value}")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if row not in range(3) or col not in range(3):
                    print("Row and column must be between 0 and 2. Try again!")
                    continue
            except ValueError:
                print("Invalid input. Please enter integers between 0 and 2.")
                continue

            # If play_move returns True, the game is over
            if self.play_move(row, col):
                break


# Run the game if the script is executed
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
