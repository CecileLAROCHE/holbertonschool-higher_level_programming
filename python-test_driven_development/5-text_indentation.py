#!/usr/bin/python3

"""
Module qui fournit une fonction text_indentation
Cette fonction permet de couper le texte
"""


def text_indentation(text):
    """
    Imprime un texte avec deux sauts de ligne après
    chaque '.', '?', ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    phrase = ""

    for char in text:
        phrase += char
        if char in ".:?":
            print(phrase.strip())
            phrase = ""

    if phrase.strip():
        print(phrase.strip())
