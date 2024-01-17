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
    def width(self):
        """width getter method"""
        return self.__width
    @property
    def height(self):
        """height getter method"""
        return self.__height
    ##setters left
