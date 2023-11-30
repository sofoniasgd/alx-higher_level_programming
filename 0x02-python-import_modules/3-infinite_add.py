#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sums = 0
    for i in range(len(argv)):
        if i == 0:
            continue
        sums += int(argv[i])
    print("{}".format(sums))
