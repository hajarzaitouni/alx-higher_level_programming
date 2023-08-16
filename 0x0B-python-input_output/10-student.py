#!/usr/bin/python3
"""
Defines Student class
"""


class Student:
    """
    creates Student classs
    """

    def __init__(self, first_name, last_name, age):
        """
        __init__ method initializes the ainstance attributes

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): The attribute name
        """
        if isinstance(attrs, list) and all(type(x) == str for x in attrs):
            new_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict
        return self.__dict__
