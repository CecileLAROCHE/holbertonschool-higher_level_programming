#!/usr/bin/python3
"""
Module contenant une fonction pour écrire une chaîne de caractères
à la fin d'un fichier texte en UTF-8.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d’un fichier texte UTF-8.
    Crée le fichier s'il n'existe pas et retourne le nombre de
    caractères ajoutés.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        nb_caracteres = f.write(text)
        return nb_caracteres
