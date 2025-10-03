#!/usr/bin/python3
"""
This module contains a function that turns JSON string to Object
"""

import json


def from_json_string(my_str):
    """
    Convert an object into a JSON string to Object
    """
    return json.dumps(my_str)
