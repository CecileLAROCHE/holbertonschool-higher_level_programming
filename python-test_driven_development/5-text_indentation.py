#!/usr/bin/python3

"""
Module qui fournit une fonction text_indentation
Cette fonction permet de couper le texte
"""


def text_indentation(text):
    """
    Imprime un texte avec deux sauts de ligne après
    chaque '.', '?', ':'
    Supprime les espaces au début et à la fin de chaque ligne.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    phrase = ""

    for char in text:
        phrase += char
        if char in ".:?":  # tous les séparateurs
            clean_phrase = phrase.strip()
            print(clean_phrase)
            print()  # saut de ligne pour <BLANKLINE>
            phrase = ""

    # Si le texte ne finit pas par un séparateur
    if phrase.strip():
        clean_phrase = phrase.strip()
        print(clean_phrase)
