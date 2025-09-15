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
        self.__size = size

    @property
    def size(self):
        """Getter : retourne la taille du carré"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : vérifie et assigne la taille"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2
