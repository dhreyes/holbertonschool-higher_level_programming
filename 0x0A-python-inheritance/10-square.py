#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py):

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from rectangle which inherits from Base """
    def __init__(self, size):
        """ initialize square """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
