import unittest

from src import Referee

class RefereeUnitTest(unittest.TestCase):
    def __init__(self):
        self.sut = Referee.Referee()

    def test_referre_should_detect_vertical_win(self):
        self.assertEquals("Won", self.sut.get_status[
            'X', 'O', 'O',
            'X', 'X', 'O',
            'X', 'O', ' ',
        ])
        self.assertEquals("Won", self.sut.get_status[
            'O', 'O', 'X'
            'X', 'O', 'O',
            'X', 'O', ' ',
        ])
        self.assertEquals("Won", self.sut.get_status[
            ' ', 'O', 'O',
            'X', 'X', 'O',
            'X', 'O', 'O',
        ])

    def test_referre_should_detect_horizontal_win(self):
        self.assertEquals("Won", self.sut.get_status[
            'O', 'O', 'O',
            'X', 'X', 'O',
            'X', 'O', 'X',
        ])
        self.assertEquals("Won", self.sut.get_status[
            'O', 'O', 'X'
            'O', 'O', 'O',
            'X', 'O', 'X',
        ])
        self.assertEquals("Won", self.sut.get_status[
            'X', 'O', 'X',
            'X', 'X', 'O',
            'O', 'O', 'O',
        ])

    def test_referre_should_detect_diagonal_win(self):
        self.assertEquals("Won", self.sut.get_status[
            'O', 'O', 'X',
            'X', 'X', 'O',
            'X', 'O', 'X',
        ])
        self.assertEquals("Won", self.sut.get_status[
            'O', 'O', 'X'
            'O', 'X', 'O',
            'X', 'O', 'X',
        ])

    def test_referre_should_detect_draw(self):
        self.assertEquals("Draw", self.sut.get_status[
            'O', 'X', 'X',
            'X', 'O', 'O',
            'X', 'O', 'X',
        ])

    def test_referre_should_detect_ongoing_game(self):
        self.assertEquals("Ongoing", self.sut.get_status[
            'O', 'X', 'X',
            'X', ' ', 'O',
            'X', 'O', 'X',
        ])