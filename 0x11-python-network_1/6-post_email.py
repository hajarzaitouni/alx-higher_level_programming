#!/usr/bin/python3
"""POST request to the passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    res = requests.post(sys.argv[1], data={'email': email})
    print(res.text)
