#!/usr/bin/python3
"""this module contain loadfromjson function"""
import json


def load_from_json_file(filename):
    """Creates an object from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
