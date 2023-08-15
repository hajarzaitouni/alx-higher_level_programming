#!/usr/bin/python3
"""
Define function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends a string at the end of text file
    and eturns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
