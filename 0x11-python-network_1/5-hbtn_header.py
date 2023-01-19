#!/usr/bin/python3
"""This module do something"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get('X-Request-Id'))
