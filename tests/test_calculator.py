""" Test for Calculator class

Command line: python -m pytest tests/test_calculator.py
"""
from math import sqrt

import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def invalid_values():
    return [
        ("1", 1, TypeError),
        (1, "1", TypeError),
        (1.0, 1, TypeError),
        (1, 1.0, TypeError),
        ("1", "1", TypeError),
        (1.0, 1.0, TypeError),
        ("a", 1.0, TypeError),
    ]


@pytest.mark.parametrize("x, y, ex", invalid_values())
def test_invalid_methods_values(calculator, x, y, ex):
    with pytest.raises(ex):
        calculator.add(x, y)
    with pytest.raises(ex):
        calculator.subtract(x, y)
    with pytest.raises(ex):
        calculator.divide(x, y)
    with pytest.raises(ex):
        calculator.multiply(x, y)
    with pytest.raises(ex):
        calculator.mod(x, y)
    with pytest.raises(ex):
        calculator.power(x, y)
    with pytest.raises(ex):
        if isinstance(x, int):
            x = 1.0
        calculator.root(x)


def test_add_method(calculator: Calculator):
    assert calculator.add(0, 0) == 0 + 0
    assert calculator.add(55, 55) == 55 + 55
    assert calculator.add(5, -6) == 5 + -6
    assert calculator.add(-2, 10) == -2 + 10
    assert calculator.add(-5, -5) == -5 + -5


def test_subtract_method(calculator: Calculator):
    assert calculator.subtract(0, 0) == 0 - 0
    assert calculator.subtract(-5, -5) == -5 - -5
    assert calculator.subtract(-15, 15) == -15 - 15
    assert calculator.subtract(15, -15) == 15 - -15
    assert calculator.subtract(10, 5) == 10 - 5


def test_divide_method(calculator: Calculator):
    with pytest.raises(ZeroDivisionError):
        assert calculator.divide(0, 0)
    assert calculator.divide(-15, 15) == -15 / 15
    assert calculator.divide(15, -15) == 15 / -15
    assert calculator.divide(10, 100) == 10 / 100
    assert calculator.divide(100, 10) == 100 / 10


def test_multiply_method(calculator: Calculator):
    assert calculator.multiply(0, 0) == 0 * 0
    assert calculator.multiply(-10, 2) == -10 * 2
    assert calculator.multiply(2, -10) == 2 * -10
    assert calculator.multiply(2, 2) == 2 * 2
    assert calculator.multiply(-5, -5) == -5 * -5


def test_mod_method(calculator: Calculator):
    with pytest.raises(ZeroDivisionError):
        assert calculator.mod(0, 0)
    assert calculator.mod(-300, 90) == -300 % 90
    assert calculator.mod(300, 90) == 300 % 90
    assert calculator.mod(7, 100) == 7 % 100
    assert calculator.mod(100, 7) == 100 % 7


def test_power_method(calculator: Calculator):
    assert calculator.power(2, 2) == 2 ** 2
    assert calculator.power(5, 0) == 5 ** 0
    assert calculator.power(1, 1) == 1 ** 1
    assert calculator.power(0, 0) == 0 ** 0
    assert calculator.power(2, 8) == 2 ** 8


def test_root_method(calculator: Calculator):
    with pytest.raises(ValueError):
        assert calculator.root(-1)
    assert calculator.root(25) == sqrt(25)
    assert calculator.root(16) == sqrt(16)
    assert calculator.root(81) == sqrt(81)
    assert calculator.root(0) == sqrt(0)
