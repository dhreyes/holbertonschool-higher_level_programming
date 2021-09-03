#!/usr/bin/python3
"""Finds a peak"""


def find_peak(list_of_integers):
    """Finds a peak"""

    if type(list_of_integers) is not list:
        return None
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[1]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[length - 1] > list_of_integers[length - 2]:
        return list_of_integers[-1]

    for idx in range(1, length):
        if (list_of_integers[idx - 1] < list_of_integers[idx] and
           list_of_integers[idx] > list_of_integers[idx + 1]):
            return list_of_integers[idx]

    return list_of_integers[0]
