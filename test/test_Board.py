import unittest

from src import Board

class BoardUnitTest(unittest.TestCase):
    def setUp(self):
        self.sut = Board.Board()

    def test_board_should_be_created_with_empty_values(self):
        self.assertEqual(self.sut.get_board(),
            [
                ' ', ' ', ' ',
                ' ', ' ', ' ',
                ' ', ' ', ' ',
            ])

    def test_board_should_be_changed_with_given_argument(self):
        self.sut.set_field(5, 'A')
        self.sut.set_field(7, 'C')
        self.sut.set_field(4, 'D')
        self.sut.set_field(1, 'X')
        self.sut.set_field(9, 'O')
        self.assertEqual(self.sut.get_board(),
            [
                'X', ' ', ' ',
                'D', 'A', ' ',
                'C', ' ', 'O',
            ])

    def test_board_should_return_value_of_field(self):
        self.test_board_should_be_changed_with_given_argument()
        self.assertEqual(self.sut.get_field(1), 'X')
        self.assertEqual(self.sut.get_field(2), ' ')
        self.assertEqual(self.sut.get_field(3), ' ')
        self.assertEqual(self.sut.get_field(4), 'D')
        self.assertEqual(self.sut.get_field(5), 'A')
        self.assertEqual(self.sut.get_field(6), ' ')
        self.assertEqual(self.sut.get_field(7), 'C')
        self.assertEqual(self.sut.get_field(8), ' ')
        self.assertEqual(self.sut.get_field(9), 'O')

    def test_board_should_define_empty_fields(self):
        self.test_board_should_be_changed_with_given_argument()
        self.assertFalse(self.sut.is_field_empty(1))
        self.assertTrue(self.sut.is_field_empty(2))
        self.assertTrue(self.sut.is_field_empty(3))
        self.assertFalse(self.sut.is_field_empty(4))
        self.assertFalse(self.sut.is_field_empty(5))
        self.assertTrue(self.sut.is_field_empty(6))
        self.assertFalse(self.sut.is_field_empty(7))
        self.assertTrue(self.sut.is_field_empty(8))
        self.assertFalse(self.sut.is_field_empty(9))