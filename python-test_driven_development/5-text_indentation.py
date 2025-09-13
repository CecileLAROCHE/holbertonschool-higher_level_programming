#!/usr/bin/python3
"""
This module contains a fonction that print some text
with 2 newlines after "." ":" and "?" characters
"""


def text_indentation(text):
    """Print text with 2 newlines after '.', ':', '?'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    start = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[start:i+1].rstrip())
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            start = i
        else:
            i += 1

    if start < len(text):
        print(text[start:].rstrip(), end="")
