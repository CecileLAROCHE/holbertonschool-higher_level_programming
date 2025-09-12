#!/usr/bin/python3

"""
Module qui fournit une fonction add_integer.
Cette fonction permet d’additionner deux entiers.
"""

def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Args:
        a (int ou float): premier nombre.
        b (int ou float, optionnel): second nombre (par défaut 98).

    Raises:
        TypeError: si a ou b ne sont pas des entiers ou des flottants.

    Returns:
        int: la somme de a et b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    
    return a + b
