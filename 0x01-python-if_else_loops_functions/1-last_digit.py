#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mod = number % -10
    print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
else:
    mod = number % 10
    if mod > 5:
        print(f"Last digit of {number} is {mod} and is greater than 5")
    elif mod == 0:
        print(f"Last digit of {number} is {mod} and is zero")
    elif mod < 6 and mod != 0:
        print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
