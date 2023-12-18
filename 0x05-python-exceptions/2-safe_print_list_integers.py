#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        ret = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except (TypeError, ValueError):
                ret += 1
                continue
    except IndexError:
        raise
    else:
        print("")
        return x - ret
