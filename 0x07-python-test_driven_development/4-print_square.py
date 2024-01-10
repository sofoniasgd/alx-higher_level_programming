#!/usr/bin/python3
"""A mdule that prints a square with'#'."""


def print_square(size):
    """Prints a square of size size with "#".

    Args:
        size (int): size/dimention of the square

    raises:
        TypeError:
    """

    error1 = "size must be an integer"
    # if size is fload and negative OR not an int->typeerror
    if isinstance(size, float) and size < 0:
        raise TypeError(error1)
    if not (isinstance(size, int) or isinstance(size, float)):
        raise TypeError(error1)
    # square cannot be of size less than 0
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end='')
        print()
