#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of a repository """
import requests
import sys


if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(sys.argv[2], sys.argv[1]))
    commit = res.json()[:10]
    for i in commit:
        print("{}: {}".format(i.get("sha"),
                              i.get("commit").get("author").get("name")))
