#!/usr/bin/python3
""" task 10 module. """


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """area method that returns area of rectangle"""

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

    def area(self):
        """returns area of a rectangle object"""

        return self.__width * self.__height

    def __str__(self):
        """str() method to return specific text"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class
    inherits from Rectangle class
    """

    def __init__(self, size):
        """validate and intialize seize attribute"""

        BaseGeometry().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method for square class"""

        return self.__size * self.__size

    def __str__(self):
        """str() method to return specific text"""

        return "[Square] {}/{}".format(self.__size, self.__size)
