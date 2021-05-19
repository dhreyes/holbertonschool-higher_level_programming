#!/usr/bin/python3
""" Getting Task 2 underway, validating input for __init__ func """


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
