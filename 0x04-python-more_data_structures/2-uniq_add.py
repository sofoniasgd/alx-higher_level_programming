#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumnumber = 0
    for i in set(my_list):
        sumnumber += i
    return sumnumber
