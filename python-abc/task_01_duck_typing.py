#!/usr/bin/env python3
'''
This module defines an abstract class Shape.
'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''
    Mother class abstract to define sub classes.
    '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''
    Class Circle that inherit from the abstract class Shape.
    '''

    def __init__(self, radius):
        """
        Initialize a circle with a radius
        """
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    '''
    Class Rectangle that inherit from the abstract class Shape.
    '''

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        """
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimetre of the rectangle"""
        return 2 * self.__width + 2 * self.__height


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
