#!/usr/bin/python3
def multiple_returns(sentence):
    first = None if sentence is None else sentence[0]
    length = len(sentence)
    return length, first
