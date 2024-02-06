#!/usr/bin/python3
"""task 4 module, defines  a json method"""


import json


def from_json_string(my_str):
    """Defines a method that returns an object from
    a json string
    Args:
        my_str (str) a json string
    """

    return json.loads(my_str)
