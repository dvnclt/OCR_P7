import time

from utils import get_top_combinations
from data import actions, budget, top_n

start_time = time.time()

top_combinations = get_top_combinations(actions, budget, top_n)

for i, (combination, total_cost, total_gain) in enumerate(top_combinations,
                                                          start=1):
    print(f"Combinaison {i} :\n"
          f"Action : Cout ; Taux")
    for action_name, action_data in combination:
        cost = action_data["cout"]
        taux = action_data["taux"]
        print(f"{action_name} : {cost:.2f}€ ; {taux*100:.2f}%")
    print(f"\nCoût total : {total_cost:.2f}€")
    print(f"Gain total : {total_gain:.2f}€\n")

end_time = time.time()

execution_time_seconds = end_time - start_time
hours, remainder = divmod(execution_time_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(
    f"Temps d'exécution : {int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    )
