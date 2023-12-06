#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1,2,4,6,8,3,5,8,9,1,2]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
