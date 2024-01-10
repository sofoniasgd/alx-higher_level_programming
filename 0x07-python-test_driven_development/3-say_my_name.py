#!/usr/bin/python3
"""A module for printing name."""


def say_my_name(first_name, last_name=""):
    """Prints full name(first_name last_name).

    Args:
        first_name (str): first name
        last_name (str): last name
    raises:
    """

    # check first_name and last_name type
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    # print name
    print("My name is {} {}".format(first_name, last_name))
