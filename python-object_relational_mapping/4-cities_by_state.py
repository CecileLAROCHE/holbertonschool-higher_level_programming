#!/usr/bin/python3
"""
Script qui se connecte à une base MySQL et affiche la ligne correspondante
à l'état rechercher
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
        db=database,
    )

    # Création du curseur
    cursor = db.cursor()

    # Exécution de la requête
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    rows = cursor.fetchall()

    # Affichage des résultats
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
