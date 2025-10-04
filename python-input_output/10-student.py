#!/usr/bin/python3
"""
Module définissant la classe Student
avec des méthodes pour obtenir une représentation JSON.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'instance.
        Si attrs est une liste de chaînes, ne renvoie que les attributs listés.
        Sinon, renvoie tous les attributs.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
