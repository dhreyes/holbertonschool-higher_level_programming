#!/usr/bin/python3
""" Getting Task 3 underway, validating input for __init__ func
    Now defining a method to find the area of class Square """


class Square:
    """ class Square with an int size equal to or greather than zero """

    def __init__(self, size=0):
        """ Function to initialize the square given the size """

        """ Validates the value passed to make sure that it meets reqs """

        """ size is the new size for the size portion of Square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the area of class Square """

        return self.__size ** 2
