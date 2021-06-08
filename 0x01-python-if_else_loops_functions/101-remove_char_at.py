#!/usr/bin/python3
def remove_char_at(str, n):
    mod_str = ""
    for index in range(0, len(str)):
        if index != n:
            mod_str += str[index]
    return (mod_str)
