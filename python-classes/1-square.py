#!/usr/bin/python3
""""
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
    def __init__(self, size):
        if size is None or not isinstance(size, int):
            raise AttributeError("'Square' object has no attribute 'size'")
        self.__size = size
