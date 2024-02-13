#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print("id:{} w:{} h:{} ".format(r1.id, r1.width, r1.height))

    r2 = Rectangle(2, 10)
    print("id:{} w:{} h:{} ".format(r2.id, r2.width, r2.height))

    r4 = Rectangle(2, 10)
    print("id:{} w:{} h:{} ".format(r4.id, r4.width, r4.height))

    r5 = Rectangle(2, 10)
    print("id:{} w:{} h:{} ".format(r5.id, r5.width, r5.height))

    r3 = Rectangle(10, 2, 0, 0, 12)
    print("id:{} w:{} h:{} x:{} y:{}".format(r3.id, r3.width, r3.height, r3.x, r3.y))

