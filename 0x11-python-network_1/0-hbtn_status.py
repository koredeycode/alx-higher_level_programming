#!/usr/bin/python3
"""This module do something"""
import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\ttype: {}".format(type(content)))
        print("\tcontent: {}".format(content))
        print("\tutf8 content: {}".format(content.decode()))
