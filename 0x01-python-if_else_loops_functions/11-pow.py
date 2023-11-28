#!/usr/bin/python3
def pow(a, b):
    num = a
    stat = 0
    if b == 0:
        return 1
    elif b < 0:
        stat = 1
        b *= -1
    for i in range(0, b - 1):
        num *= a
    if stat == 1:
        return 1/num
    else:
        return num
