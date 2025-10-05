#!/usr/bin/python3
"""
Converting CSV Data to JSON Format

Ce module définit une fonction `convert_csv_to_json` qui :
1. Lit les données d’un fichier CSV.
2. Convertit chaque ligne en dictionnaire (grâce à csv.DictReader).
3. Sauvegarde la liste de dictionnaires dans un fichier JSON nommé 'data.json'.
4. Retourne True si la conversion réussit, False en cas d'erreur.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convertit un fichier CSV en fichier JSON.
        Args:
            csv_filename (str): Le nom du fichier CSV à convertir.
        Returns:
            bool: True si la conversion a réussi, False si une erreur survient.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfiles:
            reader = csv.DictReader(csvfiles)
            rows = list(reader)
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(rows, jsonfile)
        return True
    except Exception:
        return False
