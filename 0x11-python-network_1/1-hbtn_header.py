#!/usr/bin/python3
"""This module do something"""
import urllib.request
import sys 
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
