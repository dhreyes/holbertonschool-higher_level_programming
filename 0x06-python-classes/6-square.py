#!/usr/bin/python3
""" Undergo task 6, implement position into class Square """


class Square:
    """ class Square with an int size equal to or greather than zero """
    def __init__(self, size=0, position=(0, 0)):
        """ Function to initialize the square given the size """

        """ Validates the value passed to make sure that it meets reqs """

        """ size is the new size for the size portion of Square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for iter in position:
            if type(iter) is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

        """ Also contains additional 2 loops for implementing position """
        if self.__size == 0:
            print("")
        else:
            for pos_idx_1 in range(0, self.__position[1]):
                print("")
            for x in range(0, self.__size):
                for pos_idx_0 in range(0, self.__position[0]):
                    print(" ", end="")
                for y in range(0, self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """ Class method for finding current position of Square """
        return self.__position

    @position.setter
    def position(self, value):
        """ Class method for validating and setting new position of Square """
        flag = 1
        if type(value) is tuple and len(value) == 2:
                if type(value[0]) is int and value[0] >= 0:
                    if type(value[1]) is int and value[1] >= 0:
                        self.__position = value
                        flag = 0
        if flag == 1:
            raise TypeError("position must be a tuple of 2 positive integers")
