#!/usr/bin/python3
""" Undergo task 5, implement print ability for Square """


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

    def my_print(self):
        """ Class method for Square to be printed with nested loop """
        if self.__size < 0:
            print("")
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print("")
