#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    my_item = load_from_json_file('add_item.json')
except Exception:
    my_item = []
my_item.extend(sys.argv[1:])
save_to_json_file(my_item, 'add_item.json')
