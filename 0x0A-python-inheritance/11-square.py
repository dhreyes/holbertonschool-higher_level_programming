#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the square
    description: [Square] <width>/<height>
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from rectangle which inherits from Base """
    def __init__(self, size):
        """ initialize square """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """ str rep to be able to print """
        return "[Square] {}/{}".format(self.__size, self.__size)
