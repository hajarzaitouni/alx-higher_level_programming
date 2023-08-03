#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely"""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
