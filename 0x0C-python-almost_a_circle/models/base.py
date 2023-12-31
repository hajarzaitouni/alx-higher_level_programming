#!/usr/bin/python3
"""
Defines base module
"""
import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (str): JSON string representation of list of dict
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of list of objects

        Args:
            list_objs (list): list of inherited Base instances
        """
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """laod from CSV file
        returns list of instances
        """
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                ld = csv.DictReader(f, fieldnames=fieldnames)
                ld = [{key: int(value) for key, value in dictionary.items()}
                      for dictionary in ld]
                return [cls.create(**dictionary) for dictionary in ld]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws all the Rectangles and Squares
        using turtle module

        Args:
            list_rectangles (list): list of rectangles
            list_squares (list): list of squares
        """
        turtle.Screen().bgcolor("#800080")

        t = turtle.Turtle()
        t.pensize(3)
        t.shape("turtle")
        t.speed(0)

        for rect in list_rectangles:
            t.penup()
            t.setpos(rect.x, rect.y)
            t.pendown()
            t.color("#f5f5f5")
            for i in range(2):
                t.fd(rect.width)
                t.left(90)
                t.fd(rect.height)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.setpos(square.x, square.y)
            t.pendown()
            t.color("#fceafc")
            for i in range(4):
                t.fd(square.size)
                t.left(90)

        t.hideturtle()
        turtle.exitonclick()
