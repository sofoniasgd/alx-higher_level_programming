#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args >= 1:
        str1 = ":"
    else:
        str1 = "."
    if args == 1:
        str2 = "argument"
    else:
        str2 = "arguments"
    print("{} {}".format(args, str2+str1))
    for i in range(len(argv)):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))
