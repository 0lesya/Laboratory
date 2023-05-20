import unittest
from Calc import Calc
from tkinter import *
label = Label()


class TestCalculator(unittest.TestCase):
    #def setUp(self):
    #    self.calculator = Calc(label)

    def test_sums(self):
        self.assertEqual(self.calculator.sums(4, 7), 11)

    def test_sum_float(self):
        self.assertEqual(self.calculator.sums(0.45, 0.03), 0.48)

    def test_sum_negative_num(self):
        self.assertEqual(self.calculator.sums(-12, 6), -6)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_subtract_negative_num(self):
        self.assertEqual(self.calculator.subtract(-30, 10), -40)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_multiply_float(self):
        self.assertEqual(self.calculator.multiply(0.3, 0.7), 0.21)

    def test_multiply_negative_num(self):
        self.assertEqual(self.calculator.multiply(3, -7), -21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_zero(self):
        self.assertEqual(self.calculator.divide(35, 0), "Ошибка! Попытка деления на 0")

    def test_divide_float(self):
        self.assertEqual(self.calculator.divide(1.6, 2), 0.8)

    def test_divide_negative_num(self):
        self.assertEqual(self.calculator.divide(-35, -7), 5)


if __name__ == "__main__":
    unittest.main()
