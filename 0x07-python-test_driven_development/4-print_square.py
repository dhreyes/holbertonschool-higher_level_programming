#!/usr/bin/python3
"""
0x07 project task 3
Write a function that prints a square
No importing modules
"""

def print_square(size):
    """
    Func prints a square, validates size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for x in range(0, size):
            for y in range(0, size):
                print("#", end="")
            print("")
