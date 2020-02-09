from enum import Enum

class Status(Enum):
    Win = 0,
    Draw = 1,
    Ongoing = 2,

class Referee:
    def get_status(self, board):
        pass