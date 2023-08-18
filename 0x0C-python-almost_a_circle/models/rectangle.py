#!/usr/bin/python3
"""
Define Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    creates a class that represents a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ the class constructor, initializes the instance attributes

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the x coordinate of the rectangle.
            y (int): the y coordinate of the rectangle.
            id (int): the id of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    """get the width of the Rectangle"""
    def width(self):
        return self.__width

    @width.setter
    """set the width of the Rectangle"""
    def width(self, value):
        self.__width = value

    @property
    """get the height of the Rectangle"""
    def height(self):
        return self.__height

    @height.setter
    """set the height of the Rectangle"""
    def height(self, value):
        self.__height = value

    @property
    """get the x of the Rectangle"""
    def x(self):
        return self.__x

    @x.setter
    """set the x of the Rectangle"""
    def x(self, value):
        self.__x = value

    @property
    """get the y of the Rectangle"""
    def y(self):
        return self.__y

    @y.setter
    """set the y of the Rectangle"""
    def y(self, value):
        self.__y = value
