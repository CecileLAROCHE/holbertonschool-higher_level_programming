#!/usr/bin/python3
"""
This module defines an empty Rectangle
"""


class Rectangle:
    """
        This is a Rectangle

    Args:
        width (int): largeur du rectangle (>= 0)
        height (int): hauteur du rectangle (>= 0)

    Attributes:
       __width (int): largeur privée du rectangle
        __height (int): hauteur privée du rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Setter : vérifie et assigne la width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : vérifie et assigne la height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Returns the rectangle as a string of '#' characters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Rectangle is deleted
        """
        print("Bye rectangle...")
