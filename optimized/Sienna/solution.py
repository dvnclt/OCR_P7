from data import dataset_1, dataset_2, budget
from utils import optimized_solution


# Appel de la solution optimisée pour dataset_1
best_combination, best_cost, best_gain = optimized_solution(dataset_1, budget)

# Affichage des résultats pour dataset_1
print("\nMeilleure combinaison trouvée pour dataset_1 :\n")
print("Nom action : Cout ; Taux")
for action_name, action_data in best_combination:
    print(f"{action_name} : {action_data['cout']:.2f}€ ; "
          f"{action_data['taux']*100:.2f}%")

print(f"\nCoût total : {best_cost:.2f}€ ; "
      f"Gain total sur 2 ans : {best_gain:.2f}€")


# Appel de la solution optimisée pour dataset_2
best_combination, best_cost, best_gain = optimized_solution(dataset_2, budget)

# Affichage des résultats pour dataset_2
print("\nMeilleure combinaison trouvée pour dataset_2 :\n")
print("Nom action : Cout ; Taux")
for action_name, action_data in best_combination:
    print(f"{action_name} : {action_data['cout']:.2f}€ ; "
          f"{action_data['taux']*100:.2f}%")

print(f"\nCoût total : {best_cost:.2f}€ ; "
      f"Gain total sur 2 ans : {best_gain:.2f}€")
