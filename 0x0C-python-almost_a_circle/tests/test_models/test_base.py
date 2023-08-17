#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base



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


if __name__ == '__main__':
    unittest.main()
