#!/usr/bin/python3
"""Task 8 module."""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    obj is an instance of a Class
    All attributes of the obj Class are serializable:
        list, dictionary, string, integer and boolean
    """
    return obj.__dict__
