#!/usr/bin/python3
"""
Defines base module
"""


class Base:
    """
    create Base class, the base of all other classes

    Attributes:
        nb_objects (int): the number of created instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ the class constructor, initializes the instance attributes

        Args:
            id (int): the id of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
