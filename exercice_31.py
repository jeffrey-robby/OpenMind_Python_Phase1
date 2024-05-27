def extraire_pairs_impairs(liste):
    entiers_pairs = []
    entiers_impairs = []

    for nombre in liste:
        if nombre % 2 == 0:
            entiers_pairs.append(nombre)
        else:
            entiers_impairs.append(nombre)

    return entiers_pairs, entiers_impairs

liste_nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pairs, impairs = extraire_pairs_impairs(liste_nombres)

print("Entiers pairs :", pairs)
print("Entiers impairs :", impairs)