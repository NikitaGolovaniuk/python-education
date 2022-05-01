"""An abstract game model in a philosophical sense, containing 9 empty cells lying on the
 same plane in the form of a matrix, filled with boolean values during the game.
   Rules: 1. Possible logical values are reversed every turn.
          2. the game ends when a line can be drawn between 3 identical boolean values"""


class Cell:
    """Object which can be only True or False"""

    def __init__(self):
        self.val = None


class Board:
    def __init__(self):
        rows, cols = (3, 3)
        self.matrix_board = [[Cell() for i in range(cols)] for j in range(rows)]

    def get_board(self):
        return self.matrix_board

    def get_row(self, row_num):
        return self.matrix_board[row_num]

    def get_col(self, col_num):
        return [self.matrix_board[i][col_num] for i in range(3)]

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.matrix_board[j][i].val = None


class Model:
    def __init__(self):
        self.last_turn = None
        self.board = Board()
        self.turn_count = 0

    def turn(self, row, col, turn):
        if turn != self.last_turn:
            self.board.matrix_board[col][row].val = turn
            self.turn_count += 1
            self.last_turn = turn
        else:
            raise ValueError

    def get_game_state(self):
        state = False
        if self.turn_count >= 5:
            a, b, c, d = False, False, False, False
            for i in range(3):
                if not a and not b:
                    a = self.are_all_same(
                        self.board.get_row(i)[0].val, self.board.get_row(i)[1].val, self.board.get_row(i)[2].val)
                    b = self.are_all_same(
                        self.board.get_col(i)[0].val, self.board.get_col(i)[1].val, self.board.get_col(i)[2].val)
            c = self.are_all_same(
                self.board.get_row(0)[0].val, self.board.get_row(1)[1].val, self.board.get_row(2)[2].val)
            d = self.are_all_same(
                self.board.get_row(2)[0].val, self.board.get_row(1)[1].val, self.board.get_row(0)[2].val)
            if a or b or c or d:
                state = True
        if self.turn_count == 9:
            state = True
        return state

    @staticmethod
    def are_all_same(x, y, z):
        if x is not None and y is not None and z is not None:
            if x == y == z:
                return True
            else:
                return False
        else:
            return False
