from enum import Enum

class Status(Enum):
    Win = 0,
    Draw = 1,
    Ongoing = 2,

class Referee:
    def get_status(self, board):
        if self._check_vertically(board) or self._check_horizontally(board) or self._check_diagonally(board):
            return Status.Win
        elif self._can_be_continue(board):
            return Status.Ongoing
        else:
            return Status.Draw

    def _check_vertically(self, board):
        return (board[0] == board[3] == board[6] != ' ') \
            or (board[1] == board[4] == board[7] != ' ') \
            or (board[2] == board[5] == board[8] != ' ')

    def _check_horizontally(self, board):
        return (board[0] == board[1] == board[2] != ' ') \
            or (board[3] == board[4] == board[5] != ' ') \
            or (board[6] == board[7] == board[8] != ' ') \

    def _check_diagonally(self, board):
        return (board[0] == board[4] == board[8] != ' ') \
            or (board[2] == board[4] == board[6] != ' ') \

    def _can_be_continue(self, board):
        for single_field in board:
            if single_field == ' ':
                return True
        return False