import unittest

from src import InputCheck

class TestInputCheck(unittest.TestCase):
    def setUp(self):
        self.sut = InputCheck.InputCheck()

    def test_is_in_range_0(self):
        self.assertEqual(self.sut.is_in_range(0), False)

    def test_is_in_range_1(self):
        self.assertEqual(self.sut.is_in_range(1), True)

    def test_is_in_range_2(self):
        self.assertEqual(self.sut.is_in_range(2), True)

    def test_is_in_range_3(self):
        self.assertEqual(self.sut.is_in_range(3), True)

    def test_is_in_range_4(self):
        self.assertEqual(self.sut.is_in_range(4), True)

    def test_is_in_range_5(self):
        self.assertEqual(self.sut.is_in_range(5), True)

    def test_is_in_range_6(self):
        self.assertEqual(self.sut.is_in_range(6), True)

    def test_is_in_range_7(self):
        self.assertEqual(self.sut.is_in_range(7), True)

    def test_is_in_range_8(self):
        self.assertEqual(self.sut.is_in_range(8), True)

    def test_is_in_range_9(self):
        self.assertEqual(self.sut.is_in_range(9), True)

    def test_is_in_range_10(self):
        self.assertEqual(self.sut.is_in_range(10), False)

    def test_example2(self):
        self.assertEqual(self.sut.is_in_range('Invalid message'), False)
