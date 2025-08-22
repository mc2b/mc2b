from typing import Dict, List
from src.user.profile import User

class WorkoutPlan:
    """
    Génère un plan d'entraînement hebdomadaire simple basé sur le profil et le niveau
    d'activité de l'utilisateur.
    """

    # Base de données d'exercices avec des recommandations de séries/répétitions
    EXERCISES = {
        "push": [
            "Développé couché (Bench Press) : 3 séries de 8-12 répétitions",
            "Développé militaire (Overhead Press) : 3 séries de 8-12 répétitions",
            "Pompes (Push-ups) : 3 séries jusqu'à l'échec",
            "Dips pour triceps : 3 séries de 10-15 répétitions"
        ],
        "pull": [
            "Tractions (Pull-ups or Lat Pulldowns) : 3 séries jusqu'à l'échec ou 8-12 reps",
            "Rowing avec barre (Barbell Rows) : 3 séries de 8-12 répétitions",
            "Curl biceps avec haltères : 3 séries de 10-15 répétitions"
        ],
        "legs": [
            "Squats avec barre : 3 séries de 8-12 répétitions",
            "Fentes (Lunges) : 3 séries de 10-12 répétitions par jambe",
            "Soulevé de terre roumain (Romanian Deadlift) : 3 séries de 8-12 répétitions",
            "Élévations de mollets (Calf Raises) : 3 séries de 15-20 répétitions"
        ],
        "full_body": [
            "Squats : 3 séries de 10 répétitions",
            "Développé couché : 3 séries de 10 répétitions",
            "Rowing : 3 séries de 10 répétitions",
            "Gainage (Plank) : 3 séries de 60 secondes"
        ]
    }

    def __init__(self, user: User):
        """
        Initialise le plan d'entraînement.

        Args:
            user (User): L'objet utilisateur pour lequel générer le plan.
        """
        self.user = user

    def generate_weekly_plan(self) -> Dict[str, List[str]]:
        """
        Génère un plan d'entraînement structuré pour la semaine en fonction du
        niveau d'activité de l'utilisateur.
        """
        level = self.user.activity_level

        if level in ["sédentaire", "léger"]:
            # 2 jours de full body pour construire une base solide.
            return {
                "Lundi": self.EXERCISES["full_body"],
                "Mardi": ["Repos"],
                "Mercredi": ["Repos"],
                "Jeudi": self.EXERCISES["full_body"],
                "Vendredi": ["Repos"],
                "Samedi": ["Repos"],
                "Dimanche": ["Repos"]
            }
        elif level == "modéré":
            # 3 jours en split Push/Pull/Legs pour une bonne répartition.
            return {
                "Lundi": self.EXERCISES["push"],
                "Mardi": ["Repos"],
                "Mercredi": self.EXERCISES["pull"],
                "Jeudi": ["Repos"],
                "Vendredi": self.EXERCISES["legs"],
                "Samedi": ["Repos"],
                "Dimanche": ["Repos"]
            }
        elif level in ["actif", "très actif"]:
            # 4 jours en split pour augmenter le volume et l'intensité.
            return {
                "Lundi": self.EXERCISES["push"],
                "Mardi": self.EXERCISES["pull"],
                "Mercredi": ["Repos"],
                "Jeudi": self.EXERCISES["legs"],
                "Vendredi": self.EXERCISES["push"],
                "Samedi": ["Repos"],
                "Dimanche": ["Repos"]
            }

        # Retourne un plan vide si le niveau n'est pas reconnu
        return {day: ["Repos"] for day in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]}
