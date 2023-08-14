#!/usr/bin/python3
"""
Defines is_same_class module
"""


def is_same_class(obj, a_class):
    """
    returns if the object is an instance of the specified class

    Args:
        obj (object) : the object to check
        a_class(any): type of object

    Returns: True or False
    """
    if type(obj) == a_class:
        return True
    return False
