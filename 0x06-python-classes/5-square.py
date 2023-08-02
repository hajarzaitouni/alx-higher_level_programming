#!/usr/bin/python3
"""defines a square class"""


class Square:
    """creating a class named square"""

    def __init__(self, size=0):
        """
        __init__ method initializez the size value
        of a square.

        Args:
            size (int): the size of square
        """
        self.__size = size

    def area(self):
        """calculates the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """get the size of the current square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
