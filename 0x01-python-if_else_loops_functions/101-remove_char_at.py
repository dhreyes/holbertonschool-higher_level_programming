#!/usr/bin/python3
def remove_char_at(str, n):
    mod_str = ""
    for char in range(0, len(str)):
        if char != n:
            mod_str += str[char]
    return (mod_str)
