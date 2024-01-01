#!/usr/bin/python3
"""square class module for task 0."""


class Square:
    """Define square class."""
    def __init__(self, size):
        """define private attriubte size.
        Args:
            size (int): size of a square
        """
        self.size = size

    @property
    def size(self):
        """getter property."""
        return self.__size

    @size.setter
    def size(self, size=0):
        """
        setter method chacks if the size is either
        an int of less than zero
        then raises errors if not.
        Args:
            size (int): size of a square
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >=0")
        else:
            self.__size = size
