#!/usr/bin/python3
import sys

# sys.argv[1:] crée une sous-liste contenant tous les éléments
# de sys.argv SAUF le premier (celui à l'indice 0).
# La boucle for itère ensuite sur cette sous-liste.
for argument in sys.argv[1:]:
    print(argument)

# Alternative (moins courante mais fonctionnelle) :
# Utiliser range pour commencer à l'indice 1
# for i in range(1, len(sys.argv)):
#     print(sys.argv[i])
