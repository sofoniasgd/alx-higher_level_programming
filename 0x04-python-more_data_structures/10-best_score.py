#!/usr/bin/python3
def best_score(a_dictionary):
    max_int = None
    max_key = None
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if not max_int or value > max_int:
            max_int = value
            max_key = key
    return max_key
