#!/usr/bin/python3
"""This module contain the fromjsonstring function"""
import json


def from_json_string(my_str):
    """Returns an object represented by the string"""
    return (json.loads(my_str))
