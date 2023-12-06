#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    if idx < 0:
        idx = len(my_list) + idx
    if idx >= len(my_list):
        return my_list
    for j in range(idx, len(my_list) - 1):
        my_list[j] = my_list[j + 1]
    return my_list
