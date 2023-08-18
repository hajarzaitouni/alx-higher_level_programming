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
    def width(self):
        """get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the Rectangle"""
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle"""
        self.__height = value

    @property
    def x(self):
        """get the x of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of the Rectangle"""
        self.__x = value

    @property
    def y(self):
        """get the y of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of the Rectangle"""
        self.__y = value
