#!/usr/bin/python3
def fizzbuzz():
    i = 0
    while i < 101:
        if i % 3 != 0 and i % 5 != 0:
            print("{:d}".format(i), end="")
        else:
            if i % 3 == 0:
                print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz", end="")
        if i != 100:
            print(" ", end="")
        i += 1
