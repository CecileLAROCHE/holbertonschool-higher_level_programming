#!/usr/bin/python3
"""
This module contains a fonction that print some text
with 2 newlines after "." ":" and "?" characters
"""


def text_indentation(text):
    """function that prints text with 2 newlines after '.', ':' and '?'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    phrase = ""
    for char in text:
        phrase += char
        if char in [".", ":", "?"]:
            # supprimer les espaces au début/fin de la phrase
            print(phrase.strip())
            print()  # deuxième saut de ligne
            phrase = ""

    # imprimer le reste si le texte ne finit pas par un séparateur
    if phrase.strip():
        print(phrase.strip())
