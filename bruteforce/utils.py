import itertools


# Calcule le coût total et le gain total d'une combinaison donnée
def calculate_total_cost_gain(combination):
    total_cost = 0
    total_gain = 0

    # Parcourt chaque action de la combinaison
    for action_name, action_data in combination:
        # Ajoute le coût de l'action donnée
        total_cost += action_data["cout"]
        # Calcule et ajoute le gain de l'action donnée
        total_gain += action_data["cout"] * action_data["taux"]

    return total_cost, total_gain


# Obtien les meilleures combinaisons d'actions pour un budget donné
def get_top_combinations(actions, budget, top_n):
    valid_combinations = []

    # Pour toutes les tailles de combinaisons possibles
    for r in range(1, len(actions) + 1):
        # Génère toutes les commbinaisons possibles avec Itertools
        for combination in itertools.combinations(actions.items(), r):
            # Appel de la fonction de calcul des couts / gains
            total_cost, total_gain = calculate_total_cost_gain(combination)
            # Ajoute la combinaison donnée si son coût total <= budget
            if total_cost <= budget:
                valid_combinations.append((
                    combination, total_cost, total_gain
                    ))
    # Trier les combinaisons par gain total décroissant
    top_combinations = sorted(
        valid_combinations, key=lambda x: x[2], reverse=True
        )

    return top_combinations[:top_n]
