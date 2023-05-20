import pytest
from decimal import *
from pytest_bdd import scenarios, given, when, then, parsers
from tkinter import Label
from CalcPresenter import CalcPres
label = Label()


class CalcContext:
    values = []
    result = 0

    calcul = CalcPres(label)


scenarios('loggings.feature')
Context = CalcContext


@given(parsers.parse('I have entered "{value}" into the calculator'))
@given(parsers.parse('I have entered "{value}" into the calculator'))
def start(value):
    Context.values.append(value)


@when(parsers.parse("I press {action}"))
def calculation(action):
    match action:
        case "onPlusClicked":
            Context.result = Context.calcul.onPlusClicked(Context.values[0], Context.values[1])
        case "onMinusClicked":
            Context.result = Context.calcul.onMinusClicked(Context.values[0], Context.values[1])
        case "onMultiplyClicked":
            Context.result = Context.calcul.onMultiplyClicked(Context.values[0], Context.values[1])
        case "onDivideClicked":
            Context.result = Context.calcul.onDivideClicked(Context.values[0], Context.values[1])


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
