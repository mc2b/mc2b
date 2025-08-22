from typing import Dict
from src.user.profile import User

class NutritionPlan:
    """
    Génère un plan nutritionnel personnalisé pour un utilisateur en fonction
    de ses objectifs.
    """

    ACTIVITY_MULTIPLIERS = {
        "sédentaire": 1.2,
        "léger": 1.375,
        "modéré": 1.55,
        "actif": 1.725,
        "très actif": 1.9,
    }

    def __init__(self, user: User, goal: str = "muscle_gain"):
        """
        Initialise le plan nutritionnel.

        Args:
            user (User): L'objet utilisateur pour lequel générer le plan.
            goal (str): L'objectif de l'utilisateur ('muscle_gain', 'fat_loss', 'maintenance').
        """
        self.user = user
        self.goal = goal

    def calculate_daily_calories(self) -> int:
        """
        Calcule les besoins caloriques journaliers en utilisant la formule de Mifflin-St Jeor
        pour le métabolisme de base (BMR), puis ajuste selon l'objectif.
        """
        height_cm = self.user.height * 100

        # Calcul du BMR
        if self.user.gender == "homme":
            bmr = (10 * self.user.weight) + (6.25 * height_cm) - (5 * self.user.age) + 5
        else:  # femme
            bmr = (10 * self.user.weight) + (6.25 * height_cm) - (5 * self.user.age) - 161

        # Calories pour le maintien du poids (TDEE)
        maintenance_calories = bmr * self.ACTIVITY_MULTIPLIERS[self.user.activity_level]

        # Ajustement des calories en fonction de l'objectif
        if self.goal == "muscle_gain":
            return round(maintenance_calories + 300) # Surplus calorique
        elif self.goal == "fat_loss":
            return round(maintenance_calories - 300) # Déficit calorique
        else: # maintenance
            return round(maintenance_calories)

    def get_macronutrients(self, calories: int) -> Dict[str, float]:
        """
        Répartit les calories en macronutriments (protéines, glucides, lipides).

        Args:
            calories (int): Le total de calories journalières.

        Returns:
            dict: Un dictionnaire avec les grammes de chaque macronutriment.
        """
        if self.goal == "muscle_gain":
            # 40% Glucides, 30% Protéines, 30% Lipides
            protein_grams = (calories * 0.30) / 4
            carbs_grams = (calories * 0.40) / 4
            fat_grams = (calories * 0.30) / 9
        else: # Ratio équilibré pour perte de poids ou maintien
            protein_grams = (calories * 0.25) / 4
            carbs_grams = (calories * 0.45) / 4
            fat_grams = (calories * 0.30) / 9

        return {
            "protéines_g": round(protein_grams),
            "glucides_g": round(carbs_grams),
            "lipides_g": round(fat_grams),
        }

    def get_supplement_recommendations(self) -> list[str]:
        """
        Retourne des recommandations de compléments pour la prise de muscle.
        """
        if self.goal == "muscle_gain":
            return [
                "Protéine Whey : À consommer après l'entraînement pour une récupération rapide.",
                "Créatine Monohydrate : 5g par jour pour améliorer la force et la performance.",
                "Multivitamines : Pour combler les carences nutritionnelles potentielles.",
                "Oméga-3 : Pour la santé générale et la réduction de l'inflammation."
            ]
        return []

    def generate_full_plan(self) -> Dict:
        """
        Génère et retourne le plan nutritionnel complet sous forme de dictionnaire.
        """
        calories = self.calculate_daily_calories()
        macronutrients = self.get_macronutrients(calories)
        supplements = self.get_supplement_recommendations()

        return {
            "objectif_calories_jour": calories,
            "répartition_macronutriments": macronutrients,
            "recommandations_compléments": supplements
        }
