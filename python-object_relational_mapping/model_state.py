#!/usr/bin/python3
"""
Définition du modèle State (table 'states') pour SQLAlchemy
"""
# model_state.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create an instance of declarative_base
Base = declarative_base()


# Define the State class
class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
