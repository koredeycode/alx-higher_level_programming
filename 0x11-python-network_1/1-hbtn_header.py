#!/usr/bin/python3
"""This module do something"""
import urllib.request
import sys 
url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(response.getheader('X-Request-Id'))
