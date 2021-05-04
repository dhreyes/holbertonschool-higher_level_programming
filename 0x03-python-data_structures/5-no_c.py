#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for idx in range(0, len(my_string)):
        if my_string[idx] != 'c' and my_string[idx] != 'C':
            new_str += my_string[idx]
    return new_str
