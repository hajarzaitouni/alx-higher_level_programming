#!/usr/bin/python3
""" uses the GitHub API to display your id """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get('https://api.github.com/user', auth=basic)
    print(res.json().get("id"))
