#!/usr/bin/python3
"""
this module returns returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
         returns True if the object is an instance of, or if the object is
         an instance of a class that inherited from, the specified class ;
         otherwise False.

    Args:
        None

    Attributes:
        None
    """

    return isinstance(obj, a_class)
