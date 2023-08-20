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

    def update(self, *args, **kwargs):
        """Update the class Square

        Args:
            *args (int): new attribute values
            **kwargs (dict): key/value pairs of attribute
        """
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
