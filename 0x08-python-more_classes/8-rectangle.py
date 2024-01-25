#!/usr/bin/python3
"""A Rectangle class module."""


class Rectangle:
    """Defines a rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """define private attribute width, height
        Args:
            width (): width and
            height (): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        if self.height == 0 or self.width == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """str() method to return rectangle representation
        with character #'
        """

        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        i = 0
        while i < self.height:
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            if i != (self.height - 1):
                rectangle += '\n'
            i += 1
        return rectangle

    def __repr__(self):
        """repr() method to return rectangle representation
        that can be evaluated with eval()
        """

        return "Rectangle(2, 4)"

    def __del__(self):
        """print a message when deleted."""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangle objects"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        # return rect_1 if both areas are the same or rect_1 is greater
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
