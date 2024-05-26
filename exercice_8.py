nombre_entier = int(input("Veuillez saisir un nombre entier : "))

somme = 0
for i in range(1, nombre_entier+1):
    somme = i + somme

print("La somme est de :", somme)