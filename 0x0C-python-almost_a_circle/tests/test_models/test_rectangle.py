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

    def test_display_more_args(self):
        """Testing with x and y equals to zero"""
        r1 = Rectangle(3, 4)
        with self.assertRaises(TypeError):
            r1.display(2)

    def test_str_def_args(self):
        """Testing __str__ with default args"""
        r1 = Rectangle(2, 3)
        output = "[Rectangle] ({}) 0/0 - 2/3".format(r1.id)
        self.assertEqual(str(r1), output)

    def test_str_non_defls_args(self):
        """Testing with non defaults args"""
        r1 = Rectangle(2, 5, 1, 2, 12)
        output = "[Rectangle] ({}) 1/2 - 2/5".format(r1.id)
        self.assertEqual(r1.__str__(), output)

    def test_more_args(self):
        """Testing one argument for str method"""
        r1 = Rectangle(2, 5, 1, 2, 22)
        with self.assertRaises(TypeError):
            r1.__str__(2)

    def test_update_id(self, *args):
        """Testing with one argument"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_args(self, *args):
        """Testing update with two arguments"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_args(self, *args):
        """Testing update with three args"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four_args(self):
        """Testing update with four args"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_all_args(self):
        """Testing update with all args"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        """Testing update with no args given"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")

    def test_update_two_times(self):
        """Testing update multiple times"""
        r1 = Rectangle(1, 1, 0, 0, 5)
        r1.update(89)
        r1.update(30, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (30) 10/10 - 10/10")

    def test_update_more_args(self):
        """Testing with more than five arguments"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")
        r1.height = 20
        r1.update(89, 1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_id_None(self):
        """Testing update with id=None value"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(None)
        output = "[Rectangle] ({}) 10/10 - 10/10".format(r1.id)
        self.assertEqual(str(r1), output)

    def test_update_kwargs_id(self):
        """Testing update with one kwarg id"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs_two_args(self):
        """Testing update with two kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(id=89, width=2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_kwargs_three_args(self):
        """Testing update with three kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(id=89, width=2, height=3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_kwargs_four_args(self):
        """Testing update with two kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(id=89, width=2, height=3, y=0)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/0 - 2/3")

    def test_update_kwargs_five_args(self):
        """Testing update with two kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(id=89, width=2, height=3, x=1, y=0)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/0 - 2/3")

    def test_update_kwargs_idNone(self):
        """Testing update with an id=None"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(id=None, width=2, height=3, x=1, y=0)
        output = "[Rectangle] ({}) 1/0 - 2/3".format(r1.id)
        self.assertEqual(str(r1), output)

    def test_update_no_kwargs(self):
        """Testing update with no args"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")

    def test_update_mixed_args(self):
        """Testing update with args and kwargs arguments"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(98, 2,  height=3)
        self.assertEqual(str(r1), "[Rectangle] (98) 10/10 - 2/10")
        r1.update(99, 1, 4, width=2, id=30, height=1)
        self.assertEqual(str(r1), "[Rectangle] (99) 10/10 - 1/4")

    def test_update_wrong_keys(self):
        """Testing update with args and kwargs arguments"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(w=3, h=2)
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")

    def test_update_some_wrong_keys(self):
        """Testing update with some wrong keys"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(width=3, id=98, w=3, x=2, h=2, height=4)
        self.assertEqual(str(r1), "[Rectangle] (98) 2/10 - 3/4")

    def test_update_invalid_args_RaisestypeError(self):
        """Testing update with not integer values"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, "Alx", 1, 0, 0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(89, 2, "School", 0, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(89, 2, 1, (1, 2), 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(89, 2, 1, 0, {'y': 2})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, "Alx", "School", 0, 0)

    def test_update_wid_hei_raisesValueError(self):
        """Testing update with value <= 0 for width and height"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, 0, 4, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, -2, 4, 2, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(89, 5, 0, 2, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(89, 5, -4, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, -2, -4, 2, 3)

    def test_update_x_y_raisesValueError(self):
        """Testing update with value < 0 for x and y"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 5, 4, -8, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(89, 5, 4, 2, -3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 5, 4, -8, -3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, -5, 4, -1, 0)

    def test_update_invalid_kwargs_typeError(self):
        """Testing update with invalid kwargs type"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width="invalid type")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=2.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=(1, ))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=[2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(id=89, width=3, y=[2], x=3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(id=89, height="Hello", y=[2], x=3)

    def test_update_kwargs_raisesValueError(self):
        """Testing update with value <= 0 or value < 0 for all kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=0, height=2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(id=None, width=-3, height=2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=0, width=1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(width=1, height=-2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=-2, width=-4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-2, width=3, id=13)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(x=3, y=-4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(y=-3, width=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(id=89, height=0, x=-3)

    def test_to_dict(self):
        """Testing the output to dictionary"""
        r1 = Rectangle(2, 4, 3, 2, 89)
        valid_output = {'x': 3, 'y': 2, 'id': 89, 'height': 4, 'width': 2}
        self.assertEqual(r1.to_dictionary(), valid_output)

    def test_to_dict_compare(self):
        """Testing the output with update the attributes"""
        r1 = Rectangle(2, 4, 3, 2, 89)
        r2 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_to_dict_more_args(self):
        """Testing to_dict with too many arguments"""
        r1 = Rectangle(2, 4, 3, 2, 89)
        with self.assertRaises(TypeError):
            r1.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
