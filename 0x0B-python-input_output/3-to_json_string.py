#!/usr/bin/python3
"""task 3 module, defines  a json method"""


import json


def to_json_string(my_obj):
    """Defined a method that returns a json representation
    of my_obj
    Args:
        my_obj (obj) an object
    """

    return json.dumps(my_obj)
