#!/usr/bin/python3
"""
Defines a module that prints a square.
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): size of the square

    Raises:
        TypeError: if the size is not integer
        ValueError: if the size is negative

    Return: printed Square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
