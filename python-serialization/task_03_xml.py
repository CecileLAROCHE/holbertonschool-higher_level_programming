#!/usr/bin/python3
"""
Serialization and Deserialization using XML

Ce module définit deux fonctions pour convertir un dictionnaire Python
en fichier XML et pour reconstruire un dictionnaire à partir d'un fichier XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python dans un fichier XML.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Nom du fichier XML de sortie.
    """

    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML pour reconstruire un dictionnaire Python.
    Args:
        filename (str): Nom du fichier XML à lire.
    Returns:
        dict: Le dictionnaire reconstruit à partir du XML, ou
        None si une erreur survient.
    """

    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary

    except Exception:
        return None
