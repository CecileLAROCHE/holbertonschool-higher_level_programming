#!/usr/bin/python3
"""
this module do a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    This class defines a square based on it's private attribute
    size. Size is private to ensure better control of the square.

    Args:
        size: The size of the square

    Attributes:
        size: The size of the square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
