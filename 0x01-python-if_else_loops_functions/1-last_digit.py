#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10

if digit > 5:
    words = "greater than 5"
elif digit == 0:
    words = "0"
elif digit < 6 and digit != 0:
    words = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, digit, words))
