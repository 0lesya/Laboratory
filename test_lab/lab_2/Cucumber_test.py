import pytest
from decimal import *
from pytest_bdd import scenarios, given, when, then, parsers
from tkinter import Label
from Calc import Calc

label = Label()


class CalcContext:
    values = []
    result = 0

    calcul = Calc(label)


scenarios('loggings.feature')
Context = CalcContext


@given(parsers.parse('I have entered {val:d} into the calculator'))
@given(parsers.parse('I have entered {val:d} into the calculator'))
def start(val):
    Context.values.append(val)


@when(parsers.parse("I press {action}"))
def calculation(action):
    match action:
        case "plus":
            Context.result = Context.calcul.sums(Context.values[0], Context.values[1])
        case "minus":
            Context.result = Context.calcul.subtract(Context.values[0], Context.values[1])
        case "multiply":
            Context.result = Context.calcul.multiply(Context.values[0], Context.values[1])
        case "divide":
            Context.result = Context.calcul.divide(Context.values[0], Context.values[1])


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@then(parsers.parse('the {result} should be on the screen'))
def final(result):
    if not isint(result):
        assert Context.result == result
    else:
        result = Decimal(result)
        assert Context.result == result
    Context.values = []
