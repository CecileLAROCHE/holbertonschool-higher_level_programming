#!/usr/bin/python3
"""
...
"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Récupération des arguments : username, password, database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Créer l’engine avec ces valeurs
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True)

    # Créer la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Faire la requête + afficher
    results = (
        session.query(City, State)
        .join(State)
        .order_by(City.id)
        .all()
    )

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermer la session
    session.close()
