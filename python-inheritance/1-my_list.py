#!/usr/bin/python3
"""
this module returns a class "MyList" that inherits from list:
"""


class MyList(list):
    """
        This is a blueprint of a class that defines a square.

    Args:
        None

    Attributes:
        None
    """

    def print_sorted(self):
        print(sorted(self))
