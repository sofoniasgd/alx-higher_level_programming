#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = (number * -1) % 10
else:
    last = number % 10
if number < 0:
    last *= -1
if last > 5:
    str1 = "greater than 5"
elif last == 0:
    str1 = "0"
elif last < 6 and not 0:
    str1 = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last, str1))
