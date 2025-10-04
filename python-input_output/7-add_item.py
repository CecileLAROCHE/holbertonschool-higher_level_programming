#!/usr/bin/python3
"""
Script qui ajoute tous les arguments passés en ligne de commande
dans une liste Python, puis sauvegarde cette liste au format JSON
dans le fichier add_item.json.
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    items = load_from_json_file(filename)  # lire la liste déjà enregistrée
except FileNotFoundError:
    items = []

arguments = sys.argv[1:]
items += arguments

save_to_json_file(items, filename)
