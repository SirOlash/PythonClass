from cell import Cell


class Board:
    def __init__(self):
        self._board = [[Cell.EMPTY for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self._board:
            row_values = []
            for cell in row:
                row_values.append(cell.value)
            print(" | ".join(row_values))
            print("-" * 9)

    def set_cell(self,row,col,cell:Cell):
        if self._board[row][col] == Cell.EMPTY:
            self._board[row][col]= cell
            return True
        else:
            return False

    def check_winner(self):
        for row in self._board:
            if row[0] == row[1] == row[2] != Cell.EMPTY:
                return row[0]
        for col in range(3):
            if self._board[0][col] == self._board[1][col] == self._board[2][col] != Cell.EMPTY:
                return self._board[0][col]
        if self._board[0][0] == self._board[1][1] == self._board[2][2] != Cell.EMPTY:
            return self._board[0][0]
        if self._board[0][2] == self._board[1][1] == self._board[2][0] != Cell.EMPTY:
            return self._board[0][2]
        return None

    def is_full(self):
        for row in self._board:
            for cell in row:
                if cell == Cell.EMPTY:
                    return False
        return True


