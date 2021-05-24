#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Defines a basic rectangle with width and height """

    def __init__(self, width=0, height=0):
        """ Initializes values for height and width """
        self.width = width
        self.height = height

    def __str__(self):
        """ Creates str to be returned for print statements """
        if self.area() == 0:
            return ("")
        return (("#" * self.width + "\n") * self.height)[0:-1]

    def __repr__(self):
        """ Creates standard format for instances to recreate the class """
        name = self.__class__.__name__
        rep = ("{}({}, {})".format(name, self.width, self.height))
        return rep

    def __del__(self):
        """ Gives a print message when deleting class Rectangle """
        print("Bye rectangle...")

    @property
    def width(self):
        """ Getter method for value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method for finding area of class Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Method for finding perimeter of class Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2
