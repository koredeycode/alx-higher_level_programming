#!/usr/bin/python3
"""This module do something"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:")
    print("\ttype: {}".format(type(content)))
    print("\tcontent: {}".format(content))
    print("\tutf8 content: {}".format(content.decode()))
