#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
