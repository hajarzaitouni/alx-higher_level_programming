#!usr/bin/python3
"""difine a Square class"""


class Square:
    """creating a class named Square"""

    def __init__(self, size=0):
        """
        __init__method initializes the size
        value of square.

        Args:
            size (int): the size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
