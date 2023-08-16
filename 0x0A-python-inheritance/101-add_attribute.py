#!/usr/bin/python3
"""
module that adds a new attribute to an object
"""


def add_attribute(obj, attr, value):
    """
    adds a new attribute to an object
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
