# Ecrire un programme en Python qui demande à l'utilisateur 
# de saisir deux nombres a et b et de lui afficher leur maximum, 
# sans utiliser la fonction max() ni aucune fonction prédéfinie.

# lire les valeurs de a et b
a = int(input("Tapez la valeur du nombre a : "))
b = int(input("Tapez la valeur du nombre b : "))

# Faire un test de comparaison pour trouver le plus grand 
if a > b:
    print("Le maximum  de a et de b est : a = ", a)
else:
    print("Le maximum  de a et de b est : b = ", b)
