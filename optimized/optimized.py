import time

from data import actions, budget
from utils import optimized_solution


start_time = time.time()

# Appel de la solution optimisée
best_combination, best_cost, best_gain = optimized_solution(
    actions, budget
    )

# Affichage des résultats
print("\nMeilleure combinaison trouvée :\n")
print("Nom action : Cout ; Taux")

for action_name, action_data in best_combination:
    print(f"{action_name} : {action_data['cout']:.2f}€ ; "
          f"{action_data['taux']*100:.2f}%")

print(f"\nCoût total : {best_cost:.2f}€ ; "
      f"Gain total sur 2 ans : {best_gain:.2f}€")

end_time = time.time()

execution_time_seconds = end_time - start_time
hours, remainder = divmod(execution_time_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(
    f"Temps d'exécution : {int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    )
