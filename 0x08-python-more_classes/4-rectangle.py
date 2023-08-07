#!/usr/bin/python3
"""Defines the Rectangle module"""


class Rectangle:
    """create a class representing a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        __init__ method initializes the instance attributes.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle.

        Raises:
            TypeError: if either width or height are not integers.
            ValueError: if either width or height are less than 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the printed representtation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_string = ""
        for i in range(self.__height - 1):
            rect_string += "#" * self.__width + "\n"
        rect_string += "#" * self.__width
        return rect_string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
