#!/usr/bin/python3
"""This module do something"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    values = {}
    values["email"] = sys.argv[2]
    with requests.post(url, data=values) as response:
        content = response.text
        print("{}".format(content))
