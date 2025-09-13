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
        if char in ".:?":
            print(phrase.strip())
            print()
            phrase = ""

    if phrase.strip():
        print(phrase.strip())
