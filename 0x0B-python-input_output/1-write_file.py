#!/usr/bin/python3
"""task 1 module"""


def write_file(filename="", text=""):
    """writes to a file
    Args:
        filename (str) name of file to be read
        text (str) text to be written
    function should:
        create the file if doesn’t exist
        overwrite the content of the file if it already exists
    """

    with open(filename, mode='w', encoding='utf-8') as f_file:
        return f_file.write(text)
    
