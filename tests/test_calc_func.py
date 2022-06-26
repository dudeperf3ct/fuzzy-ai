import pytest

from rpn.calc_func import add, multiply, divide, subtract, modulo

NUMBER_1 = 5
NUMBER_2 = 2


def test_add():
    assert add(NUMBER_1, NUMBER_2) == 7


def test_subtract():
    assert subtract(NUMBER_1, NUMBER_2) == 3


def test_multiply():
    assert multiply(NUMBER_1, NUMBER_2) == 10


def test_divide():
    assert divide(NUMBER_1, NUMBER_2) == 2.5


def test_modulo():
    assert modulo(NUMBER_1, NUMBER_2) == 1


def test_subtract_negative():
    assert subtract(NUMBER_2, NUMBER_1) == -3


def test_divide_by_zero():
    assert divide(NUMBER_1, 0) is None


def test_modulo_by_zero():
    assert modulo(NUMBER_1, 0) is None
