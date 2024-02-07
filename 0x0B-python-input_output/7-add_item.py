#!/usr/bin/python3
"""Task 7 module."""


import sys
import json


def add_item_to_json_file():
    """defines a method that adds all commandline
    arguments to a list and stores them in a json file
    create file if it doesnt exist
    other modules used:
    function save_to_json_file from 5-save_to_json_file.py
    function load_from_json_file from 6-load_from_json_file.py
    """

    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    list_1 = list()
    filename = "add_item.json"

    # load json file to list_1, create file if it doesnt exist
    try:
        list_1 = load_from_json(filename)
    except Exception:
        save_to_json(list_1, filename)
    # append arguments and save
    for i in range(1, len(sys.argv)):
        list_1.append(sys.argv[i])
    save_to_json(list_1, filename)


if __name__ == "__main__":
    add_item_to_json_file()
