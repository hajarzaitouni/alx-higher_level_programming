#!/usr/bin/python3
"""
inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.seek(0)
        f.write(string)
