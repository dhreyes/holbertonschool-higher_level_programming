#!/usr/bin/python3
"""
0x07 project task 0
Write function that adds two ints
No importing modules
"""


def add_integer(a, b=98):
    """
    Exceptions given for not float or int, cast into int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
