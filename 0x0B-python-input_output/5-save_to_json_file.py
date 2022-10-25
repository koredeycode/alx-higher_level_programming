#!/usr/bin/python3
"""This module contain the savetojsonfile function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
