#!/usr/bin/python3
"""
Defines base module
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of inherited Base classes
        """
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as outfile:
            if list_objs is None:
                outfile.write("[]")
            else:
                outfile.write(cls.to_json_string([cl.to_dictionary()
                                                  for cl in list_objs]))
