#!/usr/bin/python3
"""
This module contains a function that converts
a JSON string into a Python object.
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string into a Python object.
    """
    return json.loads(my_str)
