#!/usr/bin/python3
"""This module do something"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with requests.get(url) as response:
            content = response.text
            print(content)
    except requests.HTTPError as e:
        print("Error code: ", e.code)
