#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)

    Instantiation with width and height: def __init__(self, width, height)::
        width and height must be private. No getter or setter
        width and height must be positive integers validated
        by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the
    following rectangle description: [Rectangle] <width>/<height>
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ initializes new rectangle """
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        """ Find area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String rep so we can print """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
