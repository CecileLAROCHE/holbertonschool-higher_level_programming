#!/usr/bin/python3
"""
Module contenant une fonction pour lire un fichier texte en UTF-8
et afficher son contenu sur la sortie standard.
"""


def read_file(filename=""):
    """Lit un fichier texte UTF-8 et affiche son contenu sur stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
