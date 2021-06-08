#!/usr/bin/python3
"""
Initiation of square class that is a subclass of rectangle
which is a subclass of Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square with an int size equal to or greather than zero """
    err_msg = "position must be a tuple of 2 positive integers"

    def __init__(self, size, x=0, y=0, id=None):
        """ Function to initialize the square given the size """
        """ size is the new size for the size portion of Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Class method returns current size of Square """
        return self.width

    @size.setter
    def size(self, size):
        """ Class method to update the value of size aka the setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updates the attributes of rectangle to with square """
        if args is not None and len(args) is not 0:
            argc = list(args)
            if len(args) > 1:
                argc.insert(1, args[1])
            super().update(*argc)
        else:
            super().update(**kwargs)
            if "size" in kwargs:
                self.width = kwargs['size']

    def __str__(self):
        """ returns str rep of the object square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def to_dictionary(self):
        """ converts obj to dictionary format """
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.width}
