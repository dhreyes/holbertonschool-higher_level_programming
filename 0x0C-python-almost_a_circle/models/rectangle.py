#!/usr/bin/python3
""" Beginning creation of sub class of Base """
from models.base import Base


class Rectangle(Base):
    """ child class of Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize class Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @property
    def x(self):
        """ Getter method for value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for value of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter method for value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for value of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method for finding area of class Rectangle """
        return self.__height * self.__width

    def display(self):
        """ Displays the rectangle with # """
        print('\n' * self.y, end="")
        print((" " * self.x + (self.width * "#") + '\n') * self.height, end="")

    def __str__(self):
        """ returns str rep of class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        argc = len(args)
        if argc > 0:
            self.id = args[0]
            if argc > 1:
                self.width = args[1]
                if argc > 2:
                    self.height = args[2]
                    if argc > 3:
                        self.x = args[3]
                        if argc > 4:
                            self.y = args[4]
        elif kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if "height" in kwargs:
                self.height = kwargs['height']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ converts obj to dictionary format """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
