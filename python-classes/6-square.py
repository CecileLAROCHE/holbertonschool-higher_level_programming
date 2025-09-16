#!/usr/bin/python3
"""
This module defines a class Square (based on 5-square.py)
"""


class Square:
    """
    This class defines a square with private attributes __size and __position.

    Args:
        size (int): The size of the square's side (default is 0).

    Attributes:
        __size (int): Size of the square's side (private)
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter : retourne la position du carré"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter : vérifie et assigne la position"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec # et tient compte de position"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.__size):
                print(' ' * self.position[0] + '#' * self.__size)
