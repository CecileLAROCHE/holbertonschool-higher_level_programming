#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""
import sys
from model_state import State
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
    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id).all()
    )

    if states:
        for state in states:
            print(f"{state.id}: {state.name}")

    # Fermer la session
    session.close()
