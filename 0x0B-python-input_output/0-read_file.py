#!/usr/bin/python3
"""task 0 module"""


def read_file(filename=""):
    """Reads a file
    Args:
        filename (str) name of file to be read
    """

    with open(filename, 'r', encoding='utf-8') as f_file:
        text = f_file.read()
        print(text)
