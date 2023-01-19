#!/usr/bin/python3
"""This module do something"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        content = response.text
        if response.status_code < 400:
            print(content)
        else:
            print("Error code: ", response.status_code)
