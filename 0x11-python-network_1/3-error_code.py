#!/usr/bin/python3
"""This module do something"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print(content.decode())
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
