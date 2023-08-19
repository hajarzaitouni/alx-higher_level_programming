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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance"""
        for i in range(self.__y):
            print("")
        for row in range(self.__height):
            [print(" ", end="") for j in range(self.__x)]
            [print("#", end="") for col in range(self.__width)]
            print("")

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args):
        """Update the class Rectangle"""
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        super().__init__(self.__width, self.__height, self.__x,
                                         self.__y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i += 1
