#!/usr/bin/python3
"""defines a square class"""


class Square:
    """creating a class named square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ method initilaizes the size value
        of a square.

        Args:
            size (int): the size of square.
            position (tuple): position of square.
        """
        self.size = size
        self.position = position

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square to value"""
        if (type(value) != tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int) or (value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) != int) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
