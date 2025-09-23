#!/usr/bin/python3
"""
this module returns True if the object is exactly an instance
of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
        This is a blueprint of a class that defines a square.

    Args:
        None

    Attributes:
        None
    """

    return type(obj) is a_class
