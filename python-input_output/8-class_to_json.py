#!/usr/bin/python3
"""
Retourne le dictionnaire des attributs d'un objet
pour permettre sa sérialisation en JSON.
"""


def class_to_json(obj):
    attrs = vars(obj)
    return dict(attrs)
