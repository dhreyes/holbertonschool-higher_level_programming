#!/usr/bin/python3
def uppercase(str):
    for lower in str:
        if ord(lower) >= ord('a') and ord(lower) <= ord('z'):
            convert = ord('A') - ord('a')
            lower = chr(ord(lower) + convert)
        print("{}".format(lower), end="")
    print("")
