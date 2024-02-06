#!/usr/bin/python3
"""task 2 module"""


def append_write(filename="", text=""):
    """writes text to a file, must append text if file exists
    Args:
        filename (str) name of file to be read
        text (str) text to be written
    function should:
        create the file if doesn’t exist
    """

    with open(filename, mode='a', encoding='utf-8') as f_file:
        return f_file.write(text)
