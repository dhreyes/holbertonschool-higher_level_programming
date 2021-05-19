#!/usr/bin/python3
""" This is to test our ByteCode interpretation skills """
import math


class MagicClass:
    """ Magic Class for dealing with a circle """
    def __init__(self, radius=0):
        """ Method to initialize radius of the circle """
        """ Validate input for radius """
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Method to determine the area of the circle """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Method to determine the circumference of the circle """
        return 2 * math.pi * self.__radius
