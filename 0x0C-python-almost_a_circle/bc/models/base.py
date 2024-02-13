#!/usr/bin/python3
"""Base Class Module"""


class Base:
    """Define Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class
        Args:
            id (int)
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
