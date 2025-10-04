#!/usr/bin/python3
"""
Module qui définit une classe Student avec
des attributs simples et une méthode to_json().
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne le dictionnaire représentant l'instance
        """
        return self.__dict__
