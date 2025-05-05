#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un entier positif ou nul.

    Args:
        n (int): L'entier dont on veut calculer la factorielle.

    Returns:
        int: La factorielle de n, ou provoque la sortie du script
             si n est négatif.
    """
    # Gérer le cas où n est négatif (la factorielle n'est pas définie)
    if n < 0:
        print("Erreur: La factorielle n'est pas définie pour les nombres négatifs.", file=sys.stderr)
        sys.exit(1) # Quitter avec un statut d'erreur

    # Gérer le cas où n = 0 (factorielle de 0 est 1)
    if n == 0:
        return 1

    result = 1
    # Boucle tant que n est supérieur à 1
    while n > 1:
        result *= n # Multiplier le résultat par n
        n -= 1      # Décrémenter n pour l'itération suivante
    return result

# --- Section principale du script ---

# Vérifier si exactement un argument a été fourni en ligne de commande
if len(sys.argv) != 2:
    # Afficher comment utiliser le script si le nombre d'arguments est incorrect
    print(f"Usage: {sys.argv[0]} <entier positif ou nul>", file=sys.stderr)
    sys.exit(1) # Quitter avec un statut d'erreur

try:
    # Essayer de convertir le premier argument (sys.argv[1]) en entier
    number_to_calculate = int(sys.argv[1])

    # Appeler la fonction factorial avec le nombre converti
    calculated_factorial = factorial(number_to_calculate)

    # Afficher le résultat
    print(calculated_factorial)

except ValueError:
    # Gérer le cas où l'argument fourni ne peut pas être converti en entier
    print(f"Erreur: L'argument '{sys.argv[1]}' n'est pas un entier valide.", file=sys.stderr)
    sys.exit(1) # Quitter avec un statut d'erreur
