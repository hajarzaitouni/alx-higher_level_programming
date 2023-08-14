#!/usr/bin/python3
"""
Defines an inherited class checking function
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited (directly or indirectly)
    instance of a class

    Args:
        obj (object): the object to be checked.
        a_class (any): the type of the object.

    Returns: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
