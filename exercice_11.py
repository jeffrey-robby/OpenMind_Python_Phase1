nombre_entier = int(input("Veuillez saisir un nombre entier : "))

diviseurs = []

for i in range(1, nombre_entier+1):
    if nombre_entier % i == 0:
        diviseurs = [i] + diviseurs

print("Les diviseurs sont :", diviseurs)