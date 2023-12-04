#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            newstring += c
    return newstring
