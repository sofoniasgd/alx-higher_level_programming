#!/usr/bin/python3
""" task 5 module. """


class BaseGeometry():
    """BaseGeometry class(does nothing)"""

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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
