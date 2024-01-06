#!/usr/bin/python3
"""square class module for task 0."""


class Square:
    """Define square class."""
    def __init__(self, size=0):
        """define private size attribute
        Args:
            size (int): size of a square
        """
        self.size = size

    @property
    def size(self):
        """retrieve size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the attriubte size.
        check if size is an int and of less than zero value
        then raise errors if not.
        Args:
        value (int): size of a square
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Define an area method to return area of the square"""
        return self.__size * self.__size
