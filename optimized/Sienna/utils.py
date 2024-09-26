

def import_csv(csv_file):
    actions = {}

    with open(csv_file, 'r') as file:
        next(file)

        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')

                if len(parts) >= 3:
                    action_name = parts[0]
                    cout = int(float(parts[1]))
                    taux = float(parts[2]) / 100

                    # Vérification pour exclure les coûts négatifs
                    if cout >= 0:
                        actions[action_name] = {
                            'cout': cout,
                            'taux': taux
                        }
                    else:
                        print(f"Action {action_name} avec un coût négatif"
                              f"({cout}) ignorée.")

    return actions


# Calcule le gain d'une action
def calculate_gain(action):
    return action["cout"] * action["taux"]


# Fonction : Programmation dynamique (Knapsack)
def knapsack(actions, budget):
    # Table pour mémoriser les gains maximaux
    # pour chaque sous-budget de 0 à 500 (inclu)
    dp = [0] * (budget + 1)

    # Stock une liste de sous-listes
    # Chaque sous-liste contient les actions permettant un gain maximal
    # pour chaque sous-budget
    selected_actions = [[] for _ in range(budget + 1)]

    for action_name, action_data in actions.items():
        cost = action_data["cout"]
        gain = calculate_gain(action_data)

        # Parcourt la table de dp en sens inverse pour éviter d'écraser
        # les résultats intermédiaires
        for b in range(budget, cost - 1, -1):
            # budget = début de la séquence
            # cost - 1 = fin de la séquence
            # -1 = sens inverse

            # Si ajouter une action donnée améliore le gain total
            if dp[b - cost] + gain > dp[b]:
                # Met à jour la valeur de dp[b] avec le nouveau gain
                dp[b] = dp[b - cost] + gain
                # Met à jour la liste des actions sélectionnées
                selected_actions[b] = selected_actions[b - cost] + [(
                    action_name, action_data
                    )]

    # Calcul le cout total des actions sélectionnées
    total_cost = sum(
        action_data["cout"] for _, action_data in selected_actions[budget]
        )

    # Retourne la combinaison optimale, son gain total et son coût total
    return selected_actions[budget], total_cost, dp[budget]


def optimized_solution(actions, budget):

    best_combination, best_cost, best_gain = knapsack(actions, budget)

    return best_combination, best_cost, best_gain
