#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(0, len(matrix)):
        for jdx in range(0, len(matrix[idx])):
            print("{:d}".format(matrix[idx][jdx]), end="")
            if (jdx <= len(matrix[idx]) - 2):
                print(" ", end="")
        print("\n", end="")
