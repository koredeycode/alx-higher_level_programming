#!/usr/bin/python3
"""This module do something"""
import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    with requests.get(url) as response:
        info = response.json()
        for i in range(10):
            commit = info[i]
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
