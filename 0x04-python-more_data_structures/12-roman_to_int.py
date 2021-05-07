#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if roman_string is not str:
        return 0
    d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    ans = 0
    n = len(roman_string)
    for (key, value) in enumerate(roman_string):
        if key < n - 1 and d[value] < d[roman_string[key + 1]]:
            ans -= d[value]
        else:
            ans += d[value]
    return ans
