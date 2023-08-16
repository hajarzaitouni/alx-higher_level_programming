#!/usr/bin/python3
"""
Defines MyInt class, inheritor of int class
"""


class MyInt(int):
    """
    The operators == and != are inverted in MyInt class
    """

    def __eq__(self, x):
        """
        invert == operator to be != opeartor
        """
        return super().__ne__(x)

    def __ne__(self, x):
        """
        invert != operator to be ==  operator
        """
        return super().__eq__(x)
