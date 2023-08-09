#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_integer function"""

    def test_ord_list(self):
        """tests list of ordered integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unrd_list(self):
        """tests list of unordered integers"""
        self.assertEqual(max_integer([5, 6, 0, 10]), 10)

    def test_comb_list(self):
        """tests a list of combined numbers, float/int"""
        self.assertEqual(max_integer([1.2, 5, 100.6, 2]), 100.6)

    def test_neg_pos_list(self):
        """tests a list of positive and negative numbers, float/int"""
        self.assertEqual(max_integer([-1, -2.5, 0, 3]), 3)

    def test_uniq_list(self):
        """tests a list with a single element"""
        self.assertEqual(max_integer([-1]), -1)

    def test_empty_list(self):
        """tests an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_non_num_list(self):
        """tests a list of non integers/float numbers"""
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Hajar", 3, 'Z', 99.5])


if __name__ == '__main__':
    unittest.main()
