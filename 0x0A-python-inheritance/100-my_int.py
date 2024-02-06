#!/usr/bin/python3
"""task 12 module"""


class MyInt(int):
    """MyInt class
    myint is a rebel
    it has == and != operators inverted
    """

    def __init__(self, value):
        """init for myint"""

        self.value = value

    def __eq__(self, other):
        """invered == operator"""

        return not (self.__ne__(other))

    def __ne__(self, other):
        """inverted != operator """

        if isinstance(other, int):
            return (self.value == other)
        return False
