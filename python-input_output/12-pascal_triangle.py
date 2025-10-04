#!/usr/bin/python3
"""
Module qui contient une fonction pour générer le triangle de Pascal
"""


def pascal_triangle(n):
    """
    Retourne une liste de listes représentant le triangle de Pascal
    pour n lignes. Chaque ligne est une liste d'entiers.
    Retourne une liste vide si n <= 0.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        ligne = []
        for j in range(i+1):
            if j == 0 or j == i:
                ligne.append(1)
            else:
                ligne.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(ligne)

    return triangle
