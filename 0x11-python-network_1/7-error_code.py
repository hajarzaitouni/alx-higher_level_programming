#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
If the HTTP status code is >= 400, prtint Error code
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if (res.status_code >= 400):
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
