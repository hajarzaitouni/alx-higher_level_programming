#!/usr/bin/python3
"""
unittest for square class
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    Tests for Square Class
    """

    def test_Insttance_Rect(self):
        """Testing Square is instance of Rectangle and Base classes"""
        self.assertIsInstance(Square(2), Rectangle)
        self.assertIsInstance(Square(4), Base)

    def test_one_arg(self):
        """Testing with only one arguments, others are default args"""
        s1 = Square(2)
        s2 = Square(4)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s2.y, 0)

    def test_two_args(self):
        """Testing with two args, y and id arge default args"""
        s1 = Square(2, 2)
        s2 = Square(4, 1)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)

    def test_three_args(self):
        """Testing with three arguments, by default id=None"""
        s1 = Square(2, 2, 3)
        s2 = Square(4, 1, 2)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_four_args(self):
        """Testing with all arguments"""
        s1 = Square(2, 2, 3, 12)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_more_args(self):
        """Testing with more than four arguments"""
        with self.assertRaises(TypeError):
            Square(2, 2, 3, 12, 8)

    def test_no_args(self):
        """Testing square with no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_private_size(self):
        """Testing private size"""
        with self.assertRaises(AttributeError):
            print(Square(2).__size)

    def test_Attr_TypeError(self):
        """Testing arguments: size, x and y for not integer values"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hajar")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, (2, ))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, True, (2, ), 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.55, {'y': 3})

    def test_size_ValuError(self):
        """Testing size for values <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_x_ValueError(self):
        """Testing x for negative values"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1, 2, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1, 2.5, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5, -1)

    def test_y_ValueError(self):
        """Testing y for negative values"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 1, -2, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1, -2, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "invalid", -2)

    def test_area(self):
        """Testing area"""
        s1 = Square(2)
        s2 = Square(4, 1, 2, 12)
        self.assertEqual(s1.area(), 4)
        self.assertEqual(s2.area(), 16)

    def test_area_changed_size(self):
        """Testing area with changing attribute size value"""
        s1 = Square(2)
        s1.size = 3
        self.assertEqual(s1.area(), 9)

    def test_area_args(self):
        """Testing area with arguments"""
        with self.assertRaises(TypeError):
            Square(4).area(2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid").area()

    def test_display_more_args(self):
        """Testing display with more arguments"""
        with self.assertRaises(TypeError):
            Square(2).display(1)


if __name__ == '__main__':
    unittest.main()
