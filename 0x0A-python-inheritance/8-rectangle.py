#!/usr/bin/python3
""" task 8 module. """


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """area method that is empty"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate value attribute

        Args:
            name (str): always a string
            value (int):
        Raises:
            TypeError if value is not an integer
            ValueError if value is less than of equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class
    inherits from BseGeometry class
    """

    def __init__(self, width, height):
        """initialization magic method
        ckecks values of width and height
        using integer_validator of parent class
        """

        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height
