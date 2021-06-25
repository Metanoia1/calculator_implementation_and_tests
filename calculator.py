""" Home task calculator module """
from math import sqrt


class Calculator:

    """ Calculator implementation """

    def _is_valid(self, x, y=1):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Each value must be an integer instance")

    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        self._is_valid(x, y)
        return x + y

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        self._is_valid(x, y)
        return x - y

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        self._is_valid(x, y)
        return x / y

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        self._is_valid(x, y)
        return x * y

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        self._is_valid(x, y)
        return x % y

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        self._is_valid(x, y)
        return x ** y

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        self._is_valid(x)
        return sqrt(x)
