nombre_entier = int(input("Veuillez saisir un nombre entier : "))

factoriel = 1
for i in range(1, nombre_entier+1):
    factoriel = i * factoriel

print("Le factoriel de :", factoriel)