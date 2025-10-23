#!/usr/bin/python3
"""
Script qui se connecte à une base MySQL et affiche toutes les lignes
de la table 'states' dont le nom commence par 'N', triées par id croissant.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments : username, password, database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Création du curseur
    cursor = db.cursor()

    # Exécution de la requête pour récupérer tous les états commençant
    # par N triés par id
    cursor.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC;"
    )

    rows = cursor.fetchall()

    # Affichage des résultats
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
