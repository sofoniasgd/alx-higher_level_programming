#!/usr/bin/python3
def search_replace(my_list, search, replace):
    r = list(range(len(my_list)))
    return [replace if my_list[i] == search else my_list[i] for i in r]
