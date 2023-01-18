#!/usr/bin/python3
"""This module do something"""
import urllib.request
import sys
url = sys.argv[1]
values = {}
values["email"] = sys.argv[2]
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    content = response.read()
    print("{}".format(content.decode()))
