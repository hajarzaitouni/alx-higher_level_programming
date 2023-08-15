#!/usr/bin/python3
"""
Defines Square class Inheritor of Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    represent Square using Rectangle
    """

    def __init__(self, size):
        """
        __init__ method initializes the instances attributes.

        Args:
            size (int): the size of the square.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        """returns the square description"""

        return "[Square] {}/{}".format(self.__size, self.__size)
