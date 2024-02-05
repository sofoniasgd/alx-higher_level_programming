#!/usr/bin/python3
""" task 3 module. """


def is_kind_of_class(obj, a_class):
    """ checks if an object is an instance of a class.
        can also be member of parent class.
    """

    return isinstance(obj, a_class)
