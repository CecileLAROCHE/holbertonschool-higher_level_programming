#!/usr/bin/python3
"""
This module contains a fonction that print some text
with 2 newlines after "." ":" and "?" characters
"""


def text_indentation(text):
    """Print text with 2 newlines after '.', ':', '?'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    counter = 0
    phrase = ""

    for char in text:
        # ignorer les espaces en début de phrase
        if char != " ":
            counter = 0

        if char == " " and counter != 0:
            continue

        phrase += char

        # si on rencontre un séparateur
        if char in [".", ":", "?"]:
            print(phrase.strip())  # supprime les espaces au début et à la fin
            print()  # saut de ligne supplémentaire pour <BLANKLINE>
            phrase = ""
            counter = 1  # commencer à ignorer les espaces consécutifs
