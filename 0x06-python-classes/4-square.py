#!/usr/bin/python3
""" Start task 4, implementing setters and getters """


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

    @property
    def size(self):
        """ Class method returns current size of Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Class method to update the value of size aka the setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
