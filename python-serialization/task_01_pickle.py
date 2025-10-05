#!/usr/bin/python3
"""
Pickling Custom Classes

Ce module définit une classe `CustomObject` qui permet :
1. De créer un objet avec des attributs simples (nom, âge, statut étudiant).
2. De sauvegarder cet objet dans un fichier (sérialisation avec pickle).
3. De recharger un objet depuis ce fichier (désérialisation).
"""

import pickle


class CustomObject:
    """
    Une classe représentant une personne avec un nom, un âge et
    un statut étudiant.
    """

    def __init__(self, name, age, is_student):
        """
        Constructeur de la classe CustomObject.
        Args:
            name (str): Le nom de la personne.
            age (int): L’âge de la personne.
            is_student (bool): Indique si la personne est étudiante ou non.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet sous le format :
        Name: John
        Age: 25
        Is Student: True
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet courant (self) et le sauvegarde dans
        un fichier pickle.
        Args:
            filename (str): Le nom du fichier dans lequel sauvegarder l'objet.
        Si une erreur survient (ex : fichier inaccessible), la fonction doit
        gérer l'exception et retourner None.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier pickle et retourne une instance
        de CustomObject.
        Args:
            filename (str): Le nom du fichier contenant l’objet sérialisé.
        Returns:
            CustomObject: L’objet recréé à partir du fichier,
            ou None en cas d’erreur.
        """
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
                return data
        except Exception:
            return None
