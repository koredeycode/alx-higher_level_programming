#!/usr/bin/python3
"""This module contains the tojsonstring function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    return (json.dumps(my_obj))
