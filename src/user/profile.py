from typing import Literal

# Définition de types pour des attributs spécifiques afin de garantir la cohérence.
ActivityLevel = Literal["sédentaire", "léger", "modéré", "actif", "très actif"]
Gender = Literal["homme", "femme"]

class User:
    """
    Représente un utilisateur avec ses informations de base pour le suivi
    de la condition physique et de la nutrition.
    """
    def __init__(self, name: str, age: int, gender: Gender, weight: float, height: float, activity_level: ActivityLevel):
        """
        Initialise un nouvel utilisateur.

        Args:
            name (str): Le nom de l'utilisateur.
            age (int): L'âge de l'utilisateur en années.
            gender (Gender): Le sexe de l'utilisateur ('homme' ou 'femme').
            weight (float): Le poids de l'utilisateur en kilogrammes.
            height (float): La taille de l'utilisateur en mètres.
            activity_level (ActivityLevel): Le niveau d'activité physique de l'utilisateur.
        """
        if not (isinstance(age, int) and age > 0):
            raise ValueError("L'âge doit être un entier positif.")
        if not (isinstance(gender, str) and gender in ("homme", "femme")):
            raise ValueError("Le sexe doit être 'homme' ou 'femme'.")
        if not (isinstance(weight, (int, float)) and weight > 0):
            raise ValueError("Le poids doit être un nombre positif.")
        if not (isinstance(height, (int, float)) and height > 0):
            raise ValueError("La taille doit être un nombre positif.")

        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.activity_level = activity_level

    def __repr__(self) -> str:
        """
        Retourne une représentation textuelle de l'objet User pour le débogage.
        """
        return (f"User(name='{self.name}', age={self.age}, gender='{self.gender}', "
                f"weight={self.weight} kg, height={self.height} m, "
                f"activity_level='{self.activity_level}')")

    def calculate_bmi(self) -> float:
        """
        Calcule l'Indice de Masse Corporelle (IMC) de l'utilisateur.
        La formule est : poids (kg) / (taille (m))^2.

        Returns:
            float: L'IMC de l'utilisateur, arrondi à deux décimales.
        """
        if self.height <= 0:
            return 0
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)
