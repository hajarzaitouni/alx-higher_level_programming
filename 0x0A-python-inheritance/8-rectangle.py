#!/usr/bin/python3
"""
Defines Rectangle module, an inheritor of BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    represent rectangle using BaseGeometry
    """

    def __init__(self, width, height):
        """
        __init__ method initializes the instances attributes.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
