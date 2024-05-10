#!/usr/bin/python3
"""Rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instance constructor method
        Args:
            width (int): width of the rectangle
            height (int): height od the rectangle
            x (int)
            y (int)
            id (int): id of the instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # calling base class with id
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method
        Args:
            value(int)
        Raises:
            TypeError if value is not int
            ValueError if its not in range
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method
        Args:
            value(int)
        Raises:
            TypeError if value is not int
            ValueError if its not in range
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method
        Args:
            value(int)
        Raises:
            TypeError if value is not int
            ValueError if its not in range
        """

        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method
        Args:
            value(int)
        Raises:
            TypeError if value is not int
            ValueError if its not in range
        """

        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Returns area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints a rectangle (width x height) using '#'"""

        if self.__width == 0 or self.__height == 0:
            pass
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end='')
                print()
