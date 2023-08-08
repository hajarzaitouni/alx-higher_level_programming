#!/usr/bin/python3
"""
Defines a module that prints a name
"""


def say_my_name(first_name, last_name=""):
    """prints a full name

    Args:
        first_name (str): first name to print
        last_name (str): last name to print

    Raises:
        TypeError: if first/last name are not strings

    Return: a printed name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
