#!/usr/bin/python3
"""
0x07 project task 4
Write a function that prints 2 \n after [., ?, :]
No importing modules
"""

def text_indentation(text):
    """
    Validates text, and adds newlines for the special chars
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = True
    for char in text.strip():
        if char == " " and flag == True:
            continue
        print(char, end="")
        flag = False
        if char in ['.', '?', ':']:
            print('\n')
            flag = True
