from ICalculatorPresenter import CalculatorPresenter
from Calc import Calc
from CalcView import View
from decimal import *


class CalcPres(CalculatorPresenter, Calc, View):
    def onPlusClicked(self, entry_a, entry_b):
        if isinstance(entry_a, str):
            try:
                a=Decimal(entry_a)
                b=Decimal(entry_b)
                return self.printResult(self.sums(a, b))
            except:
                return self.displayError('Ошибка! Введите число')
        else:

            try:
                a = Decimal(entry_a.get())
                b = Decimal(entry_b.get())
                return self.printResult(self.sums(a, b))
            except:
                return self.displayError('Ошибка! Введите число')

    def onMinusClicked(self, entry_a, entry_b):
        if isinstance(entry_a, str):
            try:
                a=Decimal(entry_a)
                b=Decimal(entry_b)
                return self.printResult(self.subtract(a, b))
            except:
                return self.displayError('Ошибка! Введите число')
        else:
            try:
                a = Decimal(entry_a.get())
                b = Decimal(entry_b.get())
                return self.printResult(self.subtract(a, b))
            except:
                return self.displayError('Ошибка! Введите число')

    def onDivideClicked(self, entry_a, entry_b):
        if isinstance(entry_a, str):
            try:
                a=Decimal(entry_a)
                b=Decimal(entry_b)
                return self.printResult(self.divide(a, b))
            except:
                return self.displayError('Ошибка! Введите число')
        else:
            try:
                a = Decimal(entry_a.get())
                b = Decimal(entry_b.get())
                return self.printResult(self.divide(a, b))
            except:
                return self.displayError('Ошибка! Введите число')

    def onMultiplyClicked(self, entry_a, entry_b):
        if isinstance(entry_a, str):
            try:
                a=Decimal(entry_a)
                b=Decimal(entry_b)
                return self.printResult(self.multiply(a, b))
            except:
                return self.displayError('Ошибка! Введите число')
        else:
            try:
                a = Decimal(entry_a.get())
                b = Decimal(entry_b.get())
                return self.printResult(self.multiply(a, b))
            except Exception:
                return self.displayError('Ошибка! Введите число')
