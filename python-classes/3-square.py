#!/usr/bin/python3
"""
this module do a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    This class defines a square with a private attribute __size.

    Args:
        size (int): The size of the square's side (default is 0).

    Attributes:
        __size (int): Size of the square's side (private)
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2
