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

    def test_save_to_file_two_rect(self):
        """Testing saving to file two rectangles, dictionary representaion"""
        r1 = Rectangle(3, 4, 2, 1, 12)
        r2 = Rectangle(8, 2, 0, 0, 22)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 106)

    def test_save_to_file_two_square(self):
        """Testing saving to file two squares, dictionary representaion"""
        s1 = Square(4, 2, 1, 14)
        s2 = Square(8, 2, 0, 68)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 78)

    def test_save_to_file_one_square(self):
        """Testing saving to file one square using Base class"""
        s1 = Square(4, 2, 1, 14)
        Base.save_to_file([s1])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_empty_list(self):
        """Testing empty object lists"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertTrue(f.read(), "[]")

    def test_save_to_file_overwrite(self):
        """Testing overwrite the content of a file"""
        r1 = Rectangle(3, 4, 2, 1, 12)
        Rectangle.save_to_file([r1])
        s1 = Square(4, 2, 1, 14)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        """Testing None for object_lists"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertTrue(f.read(), "[]")

    def test_save_to_file_no_args(self):
        """Testing save_to_file with no arguments"""
        s1 = Square(4, 2, 1, 14)
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_more_args(self):
        """Testing save to file with more arguments"""
        s1 = Square(4, 2, 1, 14)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1], 3)


if __name__ == '__main__':
    unittest.main()
