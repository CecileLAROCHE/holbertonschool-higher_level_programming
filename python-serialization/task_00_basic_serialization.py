#!/usr/bin/python3
"""
Basic Serialization Module
This module provides two functions to:
1. Serialize a Python dictionary into a JSON file.
2. Deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it into a JSON file.

    Args:
        data (dict): Le dictionnaire Python à sérialiser.
        filename (str): Le nom du fichier JSON de sortie.

    Cette fonction convertit le dictionnaire en JSON et l’enregistre
    dans un fichier. Si le fichier existe déjà, il sera remplacé.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it back into a Python dictionary.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        dict: Le dictionnaire Python obtenu après désérialisation.

    Cette fonction lit le contenu JSON d’un fichier et le convertit
    en un dictionnaire Python.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data
