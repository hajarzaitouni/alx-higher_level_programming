#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Tests for Rectangle class
    """

    def test_deflt_args(self):
        """Testing with two arguments, x, y and id are default arg"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Testing with three args, y and id are given by default"""
        r1 = Rectangle(3, 2, 1)
        r2 = Rectangle(5, 8, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Testing with four arguments, only id is default arg"""
        r1 = Rectangle(3, 2, 1, 2)
        r2 = Rectangle(5, 8, 2, 3)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_all_args(self):
        """Testing with all arguments"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

    def test_more_than_five(self):
        """Testing more than five arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 8, 0, 0, 12, 4)

    def test_private_instances(self):
        """Testing private instances"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        with self.assertRaises(AttributeError):
            r1.__width

        with self.assertRaises(AttributeError):
            r1.__height

        with self.assertRaises(AttributeError):
            r1.__x

        with self.assertRaises(AttributeError):
            r1.__y

    def test_no_args(self):
        """Testing with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()
