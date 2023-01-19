#!/usr/bin/python3
"""This module do something"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    values = {}
    try:
        values["q"] = sys.argv[1]
    except IndexError:
        values["q"] = ""
    with requests.post(url, data=values) as response:
        try:
            obj = response.json()
            if obj == {}:
                print("No result")
            else:
                print("[{}] {}".format(obj.get("id"), obj.get("name")))
        except ValueError:
            print("Not a valid JSON")
