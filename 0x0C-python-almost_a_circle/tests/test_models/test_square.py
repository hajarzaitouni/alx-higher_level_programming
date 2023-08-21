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

    def test_str_deflt_args(self):
        """Testing str with default arguments"""
        s1 = Square(4)
        output = "[Square] ({}) 0/0 - 4".format(s1.id)
        self.assertEqual(str(s1), output)

    def test_str_non_deflts_args(self):
        """Testing str with non default arguments"""
        s1 = Square(4, 3, 2, 89)
        self.assertEqual(str(s1), "[Square] (89) 3/2 - 4")

    def test_str_more_args(self):
        """Testing str with more arguments"""
        s1 = Square(4, 3, 2, 89)
        with self.assertRaises(TypeError):
            s1.__str__(1)

    def test_update_id_args(self):
        """Testing update with one *args"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")

    def test_update_two_args(self):
        """Testing update with two args"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")

    def test_update_three_args(self):
        """Testing update with three args"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")

    def test_update_all_args(self):
        """Testing update with four args"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_more_than_four(self):
        """Testing update with more than four args"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_no_args(self):
        """Testing update with no args"""
        s1 = Square(10, 10, 10, 10)
        s1.update()
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")

    def test_update_two_times(self):
        """Testing update multiple times"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        s1.update(50)
        self.assertEqual(str(s1), "[Square] (50) 10/10 - 10")

    def test_update_changed_values(self):
        """Testing update, changing the value of attributes"""
        s1 = Square(10, 10, 10, 10)
        s1.id = 25
        s1.x = 1
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 1/10 - 10")

    def test_update_idNone(self):
        """Testing update with id=None"""
        s1 = Square(10, 10, 10, 10)
        s1.update(None)
        output = "[Square] ({}) 10/10 - 10".format(s1.id)
        self.assertEqual(str(s1), output)

    def test_update_kwargs_id(self):
        """Testing update with only one kwargs id"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(id=89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")

    def test_update_kwargs_two_args(self):
        """Testing update with two kwargs arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(id=89, x=3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 10")

    def test_update_kwargs_three_args(self):
        """Testing update with three kwargs arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(size=2, id=89, x=3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")

    def test_update_kwargs_all(self):
        """Testing update with all kwargs arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(size=2, y=4, id=89, x=3)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_kwargs_idNone(self):
        """Testing update with id=None"""
        s1 = Square(10, 10, 10, 10)
        s1.update(id=None)
        output = "[Square] ({}) 10/10 - 10".format(s1.id)
        self.assertEqual(str(s1), output)

    def test_update_kwargs_idNone_allArgs(self):
        """Testing update with all kwargs, id=None"""
        s1 = Square(10, 10, 10, 10)
        s1.update(x=1, id=None, size=4, y=2)
        output = "[Square] ({}) 1/2 - 4".format(s1.id)
        self.assertEqual(str(s1), output)

    def test_update_no_kwargs(self):
        """Testing update with no kwargs arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update()
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")

    def test_update_mixed_args(self):
        """Testing update with both args and kwargs arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 4, 1, x=1, id=30)
        self.assertEqual(str(s1), "[Square] (89) 1/10 - 4")

    def test_update_kwargs_wrong_keys(self):
        """Testing update with wrong keys"""
        s1 = Square(10, 10, 10, 10)
        s1.update(s=4, d=20)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")

    def test_update_kwargs_some_wrongKeys(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(s=4, id=89, x=2, xy=3)
        self.assertEqual(str(s1), "[Square] (89) 2/10 - 10")

    def test_update_size_TypeError(self):
        """Testing update with invalid args: size not integer"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalid", 3, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalidSize", "invalid x", 4)

    def test_update_x_TypeError(self):
        """Testing update with invalid args: x not integer"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(89, 4, [2, 3], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(89, 4, "invalid y", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalidSize", [2, 3], 2)

    def test_update_y_TypeError(self):
        """Testing update with invalid args: y not inetger"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(89, 4, 2, 3.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(89, 4, 2, (1, ))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(89, 4, "invalid x", 3.5)

    def test_update_size_ValueError(self):
        """Testing update with invalid args: size <= 0"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(89, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(89, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(89, -1, "invalid y", 3)

    def test_update_x_ValueError(self):
        """Testing update with invalid args: x < 0"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(89, 6, -3, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(89, -6, -3, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalid", -3, 2)

    def test_update_y_ValueError(self):
        """Testing update with invalid args: y < 0"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(89, 6, 3, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(89, 6, -3, -2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalid", -3, -2)

    def test_update_kwargs_size_TypeError(self):
        """Testing update with invalid kwargs: size not integer"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=4.5, id=89)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=(4, ))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(x=2, size="invalid", id=89, y=3)

    def test_update_kwargs_x_TypeError(self):
        """Testing update with invalid kwargs: x not integer"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=(2, 3), y=3, id=5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x="invalid", size=4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=[2], x="invalid", y=3, id=89)

    def test_update_kwargs_y_TypeError(self):
        """Testing update with invalid kwargs: y not integer"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(x=3, y=4.88, id=5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y={2}, x="invalid", size=4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y="j", id=89)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=[3, 2, 4], y="invalid", id=89)

    def test_update_kwargs_size_ValueError(self):
        """Testing update with invalid kwargs: size for values <= 0"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(size=0, x=2, y=3, id=89)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(size=-4, x=2, y=3, id=89)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(size=0, x=2.5, y=3, id=89)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=(1, ), size=-3, y=3, id=89)

    def test_update_kwargs_x_valueError(self):
        """Testing update with invalid kwargs: x for values < 0"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(size=3, id=89, x=-3, y=0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(x=-3, size=-2, id=89)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(x=-3, size="invalid", id=89)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y="invalid", x=-3, size=-2, id=89)

    def test_update_kwargs_y_valueError(self):
        """Testing update with invalid kwargs: y for values < 0"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(size=3, id=89, y=-3, x=2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(y=-3, size=-2, id=89)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(y=-3, size="invalid", id=89)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x="invalid", y=-3, size=-2, id=89)

    def test_to_dict(self):
        """Testing the output to dictionary"""
        s1 = Square(10, 2, 1, 89)
        valid_output = {'id': 89, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), valid_output)

    def test_to_dict_compare(self):
        """Testing with updating the attribute of a second rectangle"""
        s1 = Square(10, 2, 1, 89)
        s2 = Square(1, 1)
        s1_dictionary = s1.to_dictionary()
        s1.update(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_to_dict_more_args(self):
        """Testing to_dict with too many args"""
        s1 = Square(10, 2, 1, 89)
        with self.assertRaises(TypeError):
            s1.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
