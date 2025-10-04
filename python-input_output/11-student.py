#!/usr/bin/python3
"""
Remplace les attributs de l'instance par ceux du dictionnaire json
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
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
