import pyautogui as gui, time
gui.FAILSAFE = False
import unittest
from CalcPresenter import CalcPres
from tkinter import *
from decimal import *
label = Label()

def identifyloc():
    while True:
        currentMouseX, currentMouseY = gui.position()
        print(currentMouseX, currentMouseY)
        time.sleep(3)


class TestGui(unittest.TestCase):
    def setUp(self):
        self.calculator = CalcPres(label)

    def test_sums_norm(self):
        self.assertEqual(self.calculator.onPlusClicked('100', '4'), 'Ответ: 104')

    def test_sum_word(self):
        self.assertEqual(self.calculator.onPlusClicked('veth', 7.8), 'Ошибка! Введите число')

    def test_subtract_negative_num(self):
        self.assertEqual(self.calculator.onPlusClicked(7.8, 'veth'),  'Ошибка! Введите число')

    def test_multiply(self):
        self.assertEqual(self.calculator.onPlusClicked(100, '-='), 'Ошибка! Введите число')

    def test_minus_norm(self):
        self.assertEqual(self.calculator.onMinusClicked('100', '4'), 'Ответ: 96')

    def test_minus_word(self):
        self.assertEqual(self.calculator.onMinusClicked('veth', 7.8), 'Ошибка! Введите число')

    def test_minus_negative_num(self):
        self.assertEqual(self.calculator.onMinusClicked(7.8, 'veth'),  'Ошибка! Введите число')

    def test_minus(self):
        self.assertEqual(self.calculator.onMinusClicked(100, '-='), 'Ошибка! Введите число')

    def test_mult_norm(self):
        self.assertEqual(self.calculator.onMultiplyClicked('100', '4'), 'Ответ: 400')

    def test_mult_word(self):
        self.assertEqual(self.calculator.onMultiplyClicked('veth', 7.8), 'Ошибка! Введите число')

    def test_mult_negative_num(self):
        self.assertEqual(self.calculator.onMultiplyClicked(7.8, 'veth'),  'Ошибка! Введите число')

    def test_multiply(self):
        self.assertEqual(self.calculator.onMultiplyClicked(100, '-='), 'Ошибка! Введите число')

    def test_div_norm(self):
        self.assertEqual(self.calculator.onDivideClicked('100', '4'), 'Ответ: 25')

    def test_div_word(self):
        self.assertEqual(self.calculator.onDivideClicked('veth', 7.8), 'Ошибка! Введите число')

    def test_div_negative_num(self):
        self.assertEqual(self.calculator.onDivideClicked(7.8, 'veth'),  'Ошибка! Введите число')

    def test_div(self):
        self.assertEqual(self.calculator.onDivideClicked(100, '-='), 'Ошибка! Введите число')



screenWidth, screenHeight = gui.size()
gui.click(1653, 55)
#gui.click(x=504, y=994)
#gui.typewrite('python main.py', interval=1)
#gui.press('enter')

time.sleep(2)
list_num = ['4', 'veth', '23', '0', '7.8', '100']
list_num2 = list_num[::-1]
list_num2[-1] = '-='

for i in range(len(list_num)):
    gui.click(675, 381)
    for _ in range(len(list_num[i-1])):
        gui.press('backspace')
    gui.typewrite(list_num[i], interval=0)
    gui.click(1093, 382)
    for _ in range(len(list_num2[i-1])):
        gui.press('backspace')
    gui.typewrite(list_num2[i], interval=0)
    gui.PAUSE = 0.2
    gui.click(662, 449)
    gui.PAUSE = 0.2
    gui.click(866, 449)
    gui.PAUSE = 0.2
    gui.click(1038, 449)
    gui.PAUSE = 0.2
    gui.click(1233, 449)


gui.PAUSE = 1
gui.click(1295, 308)

unittest.main()
