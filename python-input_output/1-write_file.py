#!/usr/bin/python3
"""

"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        nb_caracteres = f.write(text)
        return nb_caracteres
