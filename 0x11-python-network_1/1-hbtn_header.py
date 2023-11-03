#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id variable
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers).get("X-Request-Id"))
