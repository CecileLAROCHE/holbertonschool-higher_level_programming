#!/usr/bin/python3
"""
this module print a square
"""


def print_square(size):
    """
    print a square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
