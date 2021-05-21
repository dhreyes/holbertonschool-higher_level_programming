#!/usr/bin/python3
"""
0x07 project task 1
Write a function that divides a matrix
No importing modules
"""
def matrix_divided(matrix, div):
    """
    Checks for valid input in matrix, implement list(map(lambda
    """
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(map(lambda y: type(y) is not list or any(map(lambda x: type(x) not in [int, float], y)), matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return list(map(lambda y: list(map(lambda x: round(x / div, 2), y)), matrix))
