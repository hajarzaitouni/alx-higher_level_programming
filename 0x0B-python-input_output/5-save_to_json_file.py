#!/usr/bin/python3
"""
Writes an Object to a text file, using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Using JSON representation, writes an object to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
