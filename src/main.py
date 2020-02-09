from InputCheck import InputCheck
from Referee import Referee
from Referee import Status
from Board import Board

current_player = "X"

def display(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


input_check = InputCheck()
referee = Referee()
board = Board()

while referee.get_status(board.get_board()) == Status.Ongoing:
    switch_player()
    display(board.get_board())
    print("It is " + current_player + '\'s turn.')
    field_number = input("Choose field (1-9): ")
    while not input_check.is_in_range(field_number):
        field_number = input("Wrong value. Choose between from 1 to 9: ")
    board.set_field(field_number, current_player)

if referee.get_status(board.get_board()) == Status.Win:
    print(current_player + ' won!')
else:
    print('Game ended with draw.')
