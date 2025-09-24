#!/usr/bin/python3
"""
This module defines a square class that inherits from rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initialize a Square with size (must be a positive integer)

    Args:
        none

    Attributes:
        __size
    """

    def __init__(self, size):
        """
        Initialize a Square with size.
        must be positive integers.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
