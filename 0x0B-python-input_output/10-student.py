#!/usr/bin/python3
"""Task 9 module"""


class Student():
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """defines a student object
        Args:
            first_name (str)
            last_name (str)
            age (str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            attributes = dict()
            for key, value in self.__dict__.items():
                for string in attrs:
                    if string == key:
                        attributes[key] = value
        return attributes
