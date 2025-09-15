#!/usr/bin/python3
""""
this module do a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    Classe représentant un carré.

    Attribut privé:
        __size (int/float): la taille du côté du carré.
    
    L'attribut est privé pour pouvoir contrôler son accès et sa modification
    dans les futures étapes (validation du type et de la valeur).
    """
    
    def __init__(self, size):
        self.__size = size
