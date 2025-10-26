#!/usr/bin/python3
"""
...
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Récupération des arguments : username, password, database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Créer l’engine avec ces valeurs
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True)

    # Créer la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Faire la requête + afficher
    state = (
        session.query(State)
        .filter_by(name=state_name)
        .order_by(State.id)
        .first()
    )

    if state:
        print(state.id)
    else:
        print("Not found")

    # Fermer la session
    session.close()
