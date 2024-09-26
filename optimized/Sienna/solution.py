from data import dataset_1, dataset_2, budget
from utils import optimized_solution, export_csv


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


# Préparer les données pour l'export
data_1 = [{'Nom action': action_name, 'Cout': action_data['cout'], 'Taux':
           f"{action_data['taux'] * 100:.2f}"
           } for action_name, action_data in best_combination]

# Ajouter une ligne vide avant les totaux
data_1.append({'Nom action': '', 'Cout': '', 'Taux': ''})
# Ajouter les totaux à la fin des données à exporter
data_1.append({'Nom action': 'Cout total :', 'Cout': f"{best_cost:.2f} €",
               'Taux': ''})  # Cout total
data_1.append({'Nom action': 'Gain total :', 'Cout': f"{best_gain:.2f} €",
               'Taux': ''})  # Gain total

# Appel de la fonction pour exporter les données
export_csv(data_1, 'data_1.csv')


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


# Préparer les données pour l'export
data_2 = [{'Nom action': action_name, 'Cout': action_data['cout'], 'Taux':
           f"{action_data['taux'] * 100:.2f}"
           } for action_name, action_data in best_combination]

# Ajouter une ligne vide avant les totaux
data_2.append({'Nom action': '', 'Cout': '', 'Taux': ''})
# Ajouter les totaux à la fin des données à exporter
data_2.append({'Nom action': 'Cout total :', 'Cout': f"{best_cost:.2f} €",
               'Taux': ''})  # Cout total
data_2.append({'Nom action': 'Gain total :', 'Cout': f"{best_gain:.2f} €",
               'Taux': ''})  # Gain total

# Appel de la fonction pour exporter les données
export_csv(data_2, 'data_2.csv')
