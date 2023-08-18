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

    def test_unique_arg(self):
        """Testing for only one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_attr_TypeError(self):
        """Testing width, height, x and y for not integer values"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(5.5, 2, 0, 0, 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2 = Rectangle("Hajar", 2, 0, 0, 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r3 = Rectangle(None, 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(10, "Alx")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5 = Rectangle(10, 2, 4.54, 0, 23)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Rectangle(10, 2, None, 0, 23)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Rectangle(10, 2, 0, [1, 2], 23)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r8 = Rectangle(10, 2, 0, None, 23)

    def test_wid_hei_ValueError(self):
        """Testing with values <= 0 for width and height attributes"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2 = Rectangle(-3, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r3 = Rectangle(2, 0)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(2, -6)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(0, 0)

    def test_x_y_ValueError(self):
        """Testing with values less than 0 for x and y attributes"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(2, 10, -1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2 = Rectangle(2, 10, -1, -2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2 = Rectangle(2, 10, 0, -2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2 = Rectangle(2, 10, 2, -3)

    def test_area(self):
        """Testing for area values"""
        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 10, 0, 0, 20)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 50)

    def test_area_args(self):
        """Testing too many args for area method"""
        r1 = Rectangle(2, 4)
        with self.assertRaises(TypeError):
            r1.area(1)

    def test_change_attr_value_area(self):
        """Testing the value area by changing width and height values"""
        r1 = Rectangle(1, 1, 0, 0, 13)
        r1.width = 2
        r1.height = 6
        self.assertEqual(r1.area(), 12)
