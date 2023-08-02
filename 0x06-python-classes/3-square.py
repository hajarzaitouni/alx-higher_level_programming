#!/usr/bin/python3
"""defines a square class"""


class Square:
    """Creating a class named Square"""

    def __init__(self, size=0):
        """
        __init__ method initilizes the size
        value of a square.

        args:
            size (int): the size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the current square area"""
        return self.__size ** 2
