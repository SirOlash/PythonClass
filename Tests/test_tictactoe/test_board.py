import unittest

from tictactoe import Board
from cell import Cell



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_that_you_can_print_board(self):
        try:
            self.board.print_board()
            actual = True
        except Exception as e:
            actual = False
        self.assertTrue(actual)


        self.assertTrue(actual)

    def test_that_you_can_set_cell(self):
        actual = self.board.set_cell(0,0,Cell.X)
        self.board.print_board()
        self.assertTrue(actual)
    def test_that_you_cannot_set_cell_to_an_already_occupied_cell(self):
        self.board.set_cell(0,0,Cell.O)
        self.board.print_board()
        self.assertFalse(self.board.set_cell(0,0,Cell.X))

    def test_that_you_can_win_vertically(self):
        self.board.set_cell(0,0,Cell.O)
        self.board.set_cell(1, 0, Cell.O)
        self.assertIsNone(self.board.check_winner())
        self.board.set_cell(2, 0, Cell.O)
        self.assertIsNotNone(self.board.check_winner())

    def test_that_you_can_win_horizontally(self):
        self.board.set_cell(0,0,Cell.O)
        self.board.set_cell(0, 1, Cell.O)
        self.assertIsNone(self.board.check_winner())
        self.board.set_cell(0, 2, Cell.O)
        self.assertIsNotNone(self.board.check_winner())

    def test_that_you_can_win_diagonally(self):
        self.board.set_cell(0,0,Cell.O)
        self.board.set_cell(1, 1, Cell.O)
        self.assertIsNone(self.board.check_winner())
        self.board.set_cell(2, 2, Cell.O)
        self.assertIsNotNone(self.board.check_winner())

    def test_that_is_full_method_works(self):
        self.board.set_cell(0,0,Cell.X)
        self.board.set_cell(1, 0, Cell.X)
        self.board.set_cell(2, 0, Cell.X)
        self.board.set_cell(0, 1, Cell.X)
        self.board.set_cell(1, 1, Cell.X)
        self.board.set_cell(2, 1, Cell.X)
        self.board.set_cell(0, 2, Cell.X)
        self.board.set_cell(1, 2, Cell.X)
        self.assertFalse(self.board.is_full())
        self.board.set_cell(2, 2, Cell.X)
        self.assertTrue(self.board.is_full())







if __name__ == '__main__':
    unittest.main()
