#!/usr/bin/python3
def add_integer(a, b=98):
    """adding two integers.

    Args:

    a (int/float): first addend
    b (int/float): second addend

    Raises:
        TypeError: If either a or b are not integers of float

    Return: Sum of two a and b;
    a and b are casted into int in the case of float

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
