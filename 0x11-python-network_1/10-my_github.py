#!/usr/bin/python3
"""This module do something"""
import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    basic = HTTPBasicAuth(user, passw)
    with requests.get('https://api.github.com/user', auth=basic) as response:
        info = response.json()
        print(info.get('id'))
