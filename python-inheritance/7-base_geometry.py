#!/usr/bin/python3
"""
this module do an empty class BaseGeometry
"""


class BaseGeometry:

    """
        do an empty class BaseGeometry

    Args:
        None

    Attributes:
        None
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
