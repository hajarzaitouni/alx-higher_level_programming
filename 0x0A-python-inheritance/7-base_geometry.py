#!/usr/bin/python3
"""
Defines BaseGeometry module
"""


class BaseGeometry:
    """
    creates BaseGeometry class
    """

    def area(self):
        """
        Area not yet Implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value as an integer

        Args:
            name (str): name of parameter.
            value (int): Value to be checked.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
