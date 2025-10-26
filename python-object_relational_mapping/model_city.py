#!/usr/bin/python3
"""
Définition du modèle City pour SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


# Define the City class
class City(Base):
    """
    City class that links to the MySQL table 'City'
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
