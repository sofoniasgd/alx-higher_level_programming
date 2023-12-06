#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumnum = 0
    for i in range(len(my_list)):
        if checklist(my_list[i:], my_list[i]):
            print(i, my_list[i])
            sumnum += my_list[i]
    return sumnum


def checklist(my_list, number):
    if len(my_list) == 1:
        return True
    for i in range(1, len(my_list)):
        if number == my_list[i]:
            return False
    return True
