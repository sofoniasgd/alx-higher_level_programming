#!/usr/bin/python3
"""
A module for Task 0.
contains add_integer function.
"""
def add_integer(a, b=98):
    """
    A function that adds two integers.
    parameters
    __________
    a : first integer
    b : second integer
    """

    # raise type error if inputs are not int or float

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    # cast a and b into int if they are float
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
import doctest
if __name__ == '__main__':
    doctest.testfile('0-add_integer.txt')
