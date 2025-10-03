#!/usr/bin/python3
"""
This module contains a function that writes
a Python object to a text file using JSON representation.
"""

import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
