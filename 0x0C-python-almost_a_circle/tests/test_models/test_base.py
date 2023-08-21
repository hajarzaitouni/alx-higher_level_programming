#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    tests for Base class
    """

    def test_no_args(self):
        """testing with no id, By default id is None"""
        b1 = Base(None)
        b2 = Base()
        b3 = Base()
        b4 = Base(None)
        b5 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b5.id - 4)

    def test_with_args(self):
        """Testing id is not None"""
        self.assertEqual((Base(20).id), 20)

    def test_None_and_not_none_id(self):
        """Testing Bases with id not None after a None ones"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, b4.id - 2)
        self.assertEqual(b3.id, 12)

    def test_nb_instance(self):
        """Testing  nb_objects as private class attribute"""
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.____nb_objects)
        with self.assertRaises(AttributeError):
            print(b1.nb_objects)

    def test_more_than_args(self):
        """ Testing more than one arguments for Base class"""
        with self.assertRaises(TypeError):
            b1 = Base(2, 3)

    def test_to_json_type(self):
        """Testing type of json string"""
        r1 = Rectangle(2, 3)
        json_dictionary = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_rect_two_dict(self):
        """Testing to_json string with only two dictionaries"""
        r1 = Rectangle(4, 8, 3, 2, 89)
        r2 = Rectangle(2, 3, 1, 0, 12)
        json_dictionary = Base.to_json_string([r1.to_dictionary(),
                                               r2.to_dictionary()])
        self.assertEqual(type(json_dictionary), str)
        self.assertTrue(len(json_dictionary) == 106)

    def test_to_json_square_type(self):
        """Testing type to_json string with square class one dict"""
        s1 = Square(4, 2, 3, 12)
        json_dictionary = Base.to_json_string([s1.to_dictionary()])
        self.assertEqual(type(json_dictionary), str)
        self.assertTrue(len(json_dictionary) == 39)

    def test_to_json_square_two_dict(self):
        """Testing type to_json string with square class, two dict"""
        s1 = Square(4, 2, 3, 12)
        s2 = Square(8, 4, 2, 6)
        json_dictionary = Base.to_json_string([s1.to_dictionary(),
                                               s2.to_dictionary()])
        self.assertEqual(type(json_dictionary), str)
        self.assertTrue(len(json_dictionary) == 77)

    def test_to_json_empty_dict(self):
        """Testing empty dictionary"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_dict_None(self):
        """Testing list of dictionaries equal to None"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_no_args(self):
        """Testing to_json_with no argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_more_args(self):
        """Testing to_json with more than one argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)


if __name__ == '__main__':
    unittest.main()
