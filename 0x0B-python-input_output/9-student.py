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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
