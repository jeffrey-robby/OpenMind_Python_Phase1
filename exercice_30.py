def valeur_commune(liste1, liste2):
    for element in liste1:
        if element in liste2:
            return True
    return False

liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 2, 8, 9, 10]

if  valeur_commune(liste1, liste2):
    print("Les listes 1 et 2 ont une valeur commune.")
else:
    print("Les listes 1 et 2 n'ont pas de valeur commune.")