#!/usr/bin/python3
"""
Script qui se connecte à une base MySQL et affiche les villes d'un état donné
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments : username, password, database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
    query = (
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name  = %s "
        "ORDER BY cities.id ASC;"
    )

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    # Affichage formaté
    names = [row[0] for row in rows]   # row[0] = cities.name
    print(", ".join(names))

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
