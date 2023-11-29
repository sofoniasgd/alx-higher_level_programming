#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            string = "Fizz"
        elif i % 5 == 0:
            string = "Buzz"
        elif i % 3 == 0 and i % 5 == 0:
            string = "FizzBuzz"
        else:
            string = str(i)
        print("{}".format(string), end=' ')
