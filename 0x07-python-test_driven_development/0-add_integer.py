#!/usr/bin/python3
"""A module for Task 0 containint addition function."""


def add_integer(a, b=98):
    """A function that adds two integers.
    Args:
    a (int or float): first integer
    b (int or float): second integer

    Raises:
        TypeError: if any of the parameters are neither int nor float
    """

    if not (isinstance(a, int) or isinstance(a, float)) or a != a:
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)) or b != b:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
