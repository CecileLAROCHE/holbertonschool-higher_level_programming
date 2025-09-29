#!/usr/bin/python3
"""
Module contenant une fonction pour écrire une chaîne de caractères
dans un fichier texte en UTF-8.
"""


def write_file(filename="", text=""):
    """Écrit une chaîne dans un fichier texte UTF-8.
    Écrase le contenu du fichier s'il existe déjà
    et retourne le nombre de caractères écrits.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        nb_caracteres = f.write(text)
        return nb_caracteres
