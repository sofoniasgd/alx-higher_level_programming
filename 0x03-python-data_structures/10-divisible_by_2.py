#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    dividebytwo = list(range(len(my_list)))
    for i in range(len(my_list)):
        dividebytwo[i] = True if my_list[i] % 2 == 0 else False
    return dividebytwo
