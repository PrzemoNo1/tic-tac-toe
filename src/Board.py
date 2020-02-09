class Board:
    def __init__(self):
        self._board = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
        ]

    def set_field(self, user_field_number, value):
        self._board[self._to_field_number(user_field_number)] = value

    def get_field(self, user_field_number):
        return self._board[self._to_field_number(user_field_number)]

    def is_field_empty(self, user_field_number):
        return self._board[self._to_field_number(user_field_number)] == ' '

    def get_board(self):
        return self._board

    def _to_field_number(self, user_field_number):
        return user_field_number - 1