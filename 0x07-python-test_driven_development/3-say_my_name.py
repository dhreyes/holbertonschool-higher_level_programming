#!/usr/bin/python3
"""
0x07 project task 2
Write a function that prints first and last name
No importing modules
"""

def say_my_name(first_name, last_name=""):
    """
    Func prints first and last name, validates str type
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
