#!/usr/bin/python3
""" sends a POST request to URL with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r = res.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except Exception:
        print("Not a valid JSON")
