#!/usr/bin/python3

def text_indentation(text):

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
