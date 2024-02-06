#!/usr/bin/python3
"""task 5 module, defines  a json method"""


import json


def save_to_json_file(my_obj, filename):
    """Defined a method that writes an object
    to a file using json representation
    Args:
        my_obj (obj) an object
        filename (str) string representing filename
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
