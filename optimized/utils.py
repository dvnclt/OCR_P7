

# Calcule le gain d'une action
def calculate_gain(action):
    return action["cout"] * action["taux"]


# Fonction 'gloutonne' pour obtenir une liste
# des actions les plus rentables en fonction du budget
def greedy_solution(actions, budget):
    # variable contenant le résultat de la fonction de trie "sorted"
    sorted_actions = sorted(
        # Génère une vue des clés / valeurs du dict actions
        actions.items(),
        # Le critère de tri est le ratio gain/cout pour chaque action
        key=lambda x: calculate_gain(x[1]) / x[1]["cout"],
        # Le tri se fait par ordre décroissant
        reverse=True
        )
    # Le but est de trier les actions
    # par ordre décroissant de rentabilité pour chaque euro dépensé

    # Liste pour stocker les actions sélectionnées
    solution = []
    # Stock le cout total des actions sélectionnées
    current_cost = 0
    # Stock le gain total des actions sélectionnées
    current_gain = 0

    # Tant que le budget le permet, ajoute les actions à la solution
    # Les actions sont ajoutées en suivant l'ordre de rentabilité
    for action_name, action_data in sorted_actions:
        # Si le cout total actuel + le cout de l'action >= budget
        if current_cost + action_data["cout"] <= budget:
            # Ajoute l'action à la liste solution
            solution.append((action_name, action_data))
            # Ajoute le cout de l'action au cout total actuel
            current_cost += action_data["cout"]
            # Ajoute le gain de l'action au gain total actuel
            current_gain += calculate_gain(action_data)

    return solution, current_cost, current_gain


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


# Essai des deux approches
def optimized_solution(actions, budget):
    # Étape 1: Solution gloutonne pour obtenir une première solution
    greedy_combination, greedy_cost, greedy_gain = greedy_solution(
        actions, budget
        )

    print("\nSolution gloutonne: \n")
    print("Nom action : Cout ; Taux")
    for action_name, action_data in greedy_combination:
        print(f"{action_name} : {action_data['cout']:.2f}€ ; "
              f"Taux : {action_data['taux']*100:.2f}%")

    print(f"\nCoût total : {greedy_cost:.2f}€, "
          f"Gain total sur 2 ans : {greedy_gain:.2f}€")

    # Étape 2: Programmation dynamique
    best_combination, best_cost, best_gain = knapsack(actions, budget)

    return best_combination, best_cost, best_gain
