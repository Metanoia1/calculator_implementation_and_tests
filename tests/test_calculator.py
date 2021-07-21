""" Test for Calculator class

Command line: python -m pytest tests/test_calculator.py
"""
from math import sqrt

from calculator import Calculator

import pytest


@pytest.fixture
def calculator():
    return Calculator()


class TestCalculator:
    def invalid_values():
        return [
            ("1", 1, TypeError),
            (1, "1", TypeError),
            (1.0, 1, TypeError),
            (1, 1.0, TypeError),
            ("1", "1", TypeError),
            (1.0, 1.0, TypeError),
            ("a", 1.0, TypeError),
            ([], 1, TypeError),
            (1, [], TypeError),
            ({}, 1, TypeError),
            (1, {}, TypeError),
        ]

    @pytest.mark.parametrize("x, y, ex", invalid_values())
    def test_invalid_add_values(self, calculator, x, y, ex):
        with pytest.raises(ex):
            calculator.add(x, y)

    @pytest.mark.parametrize("x, y, ex", invalid_values())
    def test_invalid_subtract_values(self, calculator, x, y, ex):
        with pytest.raises(ex):
            calculator.subtract(x, y)

    @pytest.mark.parametrize("x, y, ex", invalid_values())
    def test_invalid_divide_values(self, calculator, x, y, ex):
        with pytest.raises(ex):
            calculator.divide(x, y)

    @pytest.mark.parametrize("x, y, ex", invalid_values())
    def test_invalid_multiply_values(self, calculator, x, y, ex):
        with pytest.raises(ex):
            calculator.multiply(x, y)

    @pytest.mark.parametrize("x, y, ex", invalid_values())
    def test_invalid_mod_values(self, calculator, x, y, ex):
        with pytest.raises(ex):
            calculator.mod(x, y)

    @pytest.mark.parametrize("x, y, ex", invalid_values())
    def test_invalid_power_values(self, calculator, x, y, ex):
        with pytest.raises(ex):
            calculator.power(x, y)

    @pytest.mark.parametrize(
        "x, ex",
        [
            ("1", TypeError),
            (1.0, TypeError),
            ("a", TypeError),
            ([], TypeError),
            ({}, TypeError),
        ],
    )
    def test_invalid_root_values(self, calculator, x, ex):
        with pytest.raises(ex):
            calculator.root(x)

    @pytest.mark.parametrize(
        "x, y, result",
        [
            (0, 0, 0),
            (55, 55, 110),
            (5, -6, -1),
            (-2, 10, 8),
            (-5, -5, -10),
        ],
    )
    def test_add_method(self, calculator, x, y, result):
        assert calculator.add(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result",
        [
            (0, 0, 0),
            (-5, -5, 0),
            (-15, 15, -30),
            (15, -15, 30),
            (10, 5, 5),
        ],
    )
    def test_subtract_method(self, calculator, x, y, result):
        assert calculator.subtract(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result",
        [
            (-15, 15, -1),
            (15, -15, -1),
            (10, 100, 0.1),
            (100, 10, 10),
        ],
    )
    def test_divide_method(self, calculator, x, y, result):
        assert calculator.divide(x, y) == result
        with pytest.raises(ZeroDivisionError):
            assert calculator.divide(0, 0)

    @pytest.mark.parametrize(
        "x, y, result",
        [
            (0, 0, 0),
            (-10, 2, -20),
            (2, -10, -20),
            (2, 2, 4),
            (-5, -5, 25),
        ],
    )
    def test_multiply_method(self, calculator, x, y, result):
        assert calculator.multiply(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result",
        [
            (-300, 90, 60),
            (300, 90, 30),
            (7, 100, 7),
            (100, 7, 2),
        ],
    )
    def test_mod_method(self, calculator, x, y, result):
        assert calculator.mod(x, y) == result
        with pytest.raises(ZeroDivisionError):
            assert calculator.mod(0, 0)

    @pytest.mark.parametrize(
        "x, y, result",
        [
            (2, 2, 4),
            (5, 0, 1),
            (1, 1, 1),
            (0, 0, 1),
            (2, 8, 256),
        ],
    )
    def test_power_method(self, calculator, x, y, result):
        assert calculator.power(x, y) == result

    @pytest.mark.parametrize(
        "x, result",
        [
            (25, 5),
            (16, 4),
            (81, 9),
            (0, 0),
        ],
    )
    def test_root_method(self, calculator, x, result):
        assert calculator.root(x) == result
        with pytest.raises(ValueError):
            assert calculator.root(-1)
