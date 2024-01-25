#!/usr/bin/python3
def best_score(a_dictionary):
    maxint = None
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if not maxint or value > maxint:
            maxint = value
    return maxint
