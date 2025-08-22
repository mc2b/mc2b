from src.user.profile import User
from src.nutrition.plan import NutritionPlan
from src.workout.plan import WorkoutPlan
import json

def main():
    """
    Fonction principale pour démontrer la génération de plans de nutrition et d'entraînement.
    """
    # 1. Créer un profil utilisateur de démonstration
    # User(name, age, gender, weight_kg, height_m, activity_level)
    # Niveaux d'activité possibles : "sédentaire", "léger", "modéré", "actif", "très actif"
    # Objectifs possibles : "muscle_gain", "fat_loss", "maintenance"
    user = User(
        name="Alex Moreau",
        age=30,
        gender="homme",
        weight=75.0,
        height=1.80,
        activity_level="modéré"
    )

    print("="*50)
    print(f"PROFIL UTILISATEUR : {user.name}")
    print("="*50)
    print(user)
    print(f"IMC (Indice de Masse Corporelle) : {user.calculate_bmi()}")
    print("\n")

    # 2. Générer le plan nutritionnel
    nutrition_plan_generator = NutritionPlan(user, goal="muscle_gain")
    full_nutrition_plan = nutrition_plan_generator.generate_full_plan()

    print("="*50)
    print(f"PLAN NUTRITIONNEL (Objectif : {nutrition_plan_generator.goal})")
    print("="*50)
    # Utiliser json.dumps pour un affichage propre du dictionnaire
    print(json.dumps(full_nutrition_plan, indent=4, ensure_ascii=False))
    print("\n")

    # 3. Générer le plan d'entraînement
    workout_plan_generator = WorkoutPlan(user)
    weekly_workout_plan = workout_plan_generator.generate_weekly_plan()

    print("="*50)
    print("PLAN D'ENTRAÎNEMENT HEBDOMADAIRE")
    print("="*50)
    for day, exercises in weekly_workout_plan.items():
        print(f"--- {day} ---")
        if "Repos" in exercises[0]:
            print("Repos")
        else:
            for exercise in exercises:
                print(f"- {exercise}")
        print()

if __name__ == "__main__":
    main()
