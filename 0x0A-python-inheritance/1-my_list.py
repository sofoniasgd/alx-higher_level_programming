#!/usr/bin/python3
""" task 1 module. """


class MyList(list):
    """ MyList class for task 1. """

    def print_sorted(self):
        """ prints sorted list in ascending order. """

        # create a copy because sort() works in place
        tobesorted = self[:]
        tobesorted.sort()
        print(tobesorted)
