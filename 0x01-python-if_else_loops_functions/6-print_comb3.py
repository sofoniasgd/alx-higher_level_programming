#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i*10 + j) > (j*10 + i) or (i == j):
            continue
        if (i*10 + j) < 89:
            print("{:02d}".format(i*10 + j), end=', ')
        else:
            print("{}".format(i*10 + j))
