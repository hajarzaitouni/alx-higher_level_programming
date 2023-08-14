#!/usr/bin/python3
"""
defines is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    returns if the object is an instance of
    or inherited instance of class

    Args:
        obj (object): the object to be checked.
        a_class (any): type of object.

    Returns:
        True or False
    """

    if isinstance(obj, a_class):
        return True
    return False
