#!/usr/bin/python3
"""square class module for task 0."""


class Square:
    """Define square class."""
    def __init__(self, size=0):
        """define private attriubte size.
        check size is an int and of less than zero value
        then raises errors if not.
        Args:
            size (int): size of a square
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
