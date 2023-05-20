from ICalculator import Calculator
from CalcView import View
from decimal import *


class Calc(Calculator, View):

    def sums(self, a: Decimal, b: Decimal) -> Decimal:
        return a+b

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        return a-b

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        return a*b

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        try:
            return a/b
        except ZeroDivisionError:
            return self.displayError("Ошибка! Попытка деления на 0")



