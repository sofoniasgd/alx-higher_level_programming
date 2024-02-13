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
            x
            y
            id
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

        @property
        def height(self):
            """getter method for height"""
            return self.__height

        @property
        def x(self):
            """getter method for x"""
            return self.__x

        @property
        def y(self):
            """getter method for y"""
            return self.__y

        @property
        def id(self):
            """getter method for id"""
            return self.__id

        @width.setter
        def width(self, value):
            """width setter method"""
            self.__width = value

        @height.setter
        def height(self, value):
            """height setter method"""
            self.__height = value

        @x.setter
        def x(self, value):
            """x setter method"""
            self.__x = value

        @y.setter
        def y(self, value):
            """y setter method"""
            self.__y = value
