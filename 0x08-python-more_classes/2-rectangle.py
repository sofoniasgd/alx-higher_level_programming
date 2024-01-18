#!/usr/bin/python3
"""A Rectangle class module."""


class Rectangle:
    """Defines a rectangle class."""

    def __init__(self, width=0, height=0):
        """define private attribute width, height
        Args:
            width (): width and
            height (): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter for height attribute
        checks if value is an integer
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @width.setter
    def width(self, value):
        """setter for width attribute
        checks if value is an integer
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Returns area of the rectangle."""

        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the rectangle."""

        return (self.width * 2) + (self.height * 2)
