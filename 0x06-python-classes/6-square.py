#!/usr/bin/python3
"""square class module for task 0."""


class Square:
    """Define square class."""
    def __init__(self, size=0, position=(0, 0)):
        """define private size attribute
        Args:
            size (int): size of a square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieve size attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the attriubte position.
        check if size is a tuple and exactly two values
        then raise errors if not.
        Args:
        value (int): size of a square
        """
        check = isinstance(value, tuple) and len(value) == 2
        check = check and isinstance(value[0], int) and value[0] >= 0
        check = check and isinstance(value[1], int) and value[1] >= 0
        if (not check):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Define an area method to return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints (in stdout) the square with character '#' """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
