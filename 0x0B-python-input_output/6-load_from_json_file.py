#!/usr/bin/python3
"""task 6 module, defines  a json method"""


import json


def load_from_json_file(filename):
    """Defines a method that creates an object from
    a json file
    Args:
        filename (str) a json file filename
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
