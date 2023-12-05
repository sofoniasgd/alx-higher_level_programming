#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    for i in range(2):
        x = tuple_a[i] if i < len(tuple_a) else 0
        y = tuple_b[i] if i < len(tuple_b) else 0
        a += [x + y]
    return (a[0], a[1])
