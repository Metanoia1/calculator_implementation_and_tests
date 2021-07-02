""" Test for Calculator class

Command line: python -m pytest tests/test_calculator.py
"""
from math import sqrt

from calculator import Calculator

import pytest


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
            x = str(x)
        calculator.root(x)


@pytest.mark.parametrize(
    "x, y",
    [
        (0, 0),
        (55, 55),
        (5, -6),
        (-2, 10),
        (-5, -5),
    ],
)
def test_add_method(calculator, x, y):
    assert calculator.add(x, y) == x + y


@pytest.mark.parametrize(
    "x, y",
    [
        (0, 0),
        (-5, -5),
        (-15, 15),
        (15, -15),
        (10, 5),
    ],
)
def test_subtract_method(calculator, x, y):
    assert calculator.subtract(x, y) == x - y


@pytest.mark.parametrize(
    "x, y",
    [
        (-15, 15),
        (15, -15),
        (10, 100),
        (100, 10),
    ],
)
def test_divide_method(calculator, x, y):
    assert calculator.divide(x, y) == x / y
    with pytest.raises(ZeroDivisionError):
        assert calculator.divide(0, 0)


@pytest.mark.parametrize(
    "x, y",
    [
        (0, 0),
        (-10, 2),
        (2, -10),
        (2, 2),
        (-5, -5),
    ],
)
def test_multiply_method(calculator, x, y):
    assert calculator.multiply(x, y) == x * y


@pytest.mark.parametrize(
    "x, y",
    [
        (-300, 90),
        (300, 90),
        (7, 100),
        (100, 7),
    ],
)
def test_mod_method(calculator, x, y):
    assert calculator.mod(x, y) == x % y
    with pytest.raises(ZeroDivisionError):
        assert calculator.mod(0, 0)


@pytest.mark.parametrize(
    "x, y",
    [
        (2, 2),
        (5, 0),
        (1, 1),
        (0, 0),
        (2, 8),
    ],
)
def test_power_method(calculator, x, y):
    assert calculator.power(x, y) == x ** y


@pytest.mark.parametrize(
    "x",
    [
        (25),
        (16),
        (81),
        (0),
    ],
)
def test_root_method(calculator, x):
    assert calculator.root(x) == sqrt(x)
    with pytest.raises(ValueError):
        assert calculator.root(-1)
