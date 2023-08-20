#!/usr/bin/python3
"""
Defines Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    creates a class that represents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ contructor initializes the instance attributes

        Args:
            size (int): the size of the square
            x (int): the x coordinate of the square.
            y (int): the y coordinate of the square.
            id (int): the id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns the square description"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
