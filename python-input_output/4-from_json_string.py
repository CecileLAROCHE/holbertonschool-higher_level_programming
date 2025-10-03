#!/usr/bin/python3
import json
"""
This module contains a function that turns JSON string to Object
"""


def from_json_string(my_str):
    """
    Convert an object into a JSON string to Object
    """
    return json.dumps(my_str)
