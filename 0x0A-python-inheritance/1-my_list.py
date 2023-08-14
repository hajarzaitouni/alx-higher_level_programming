#!/usr/bin/python3
"""
Defines MyList module
"""


class MyList(list):
    """
    creates MyList class
    """
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
