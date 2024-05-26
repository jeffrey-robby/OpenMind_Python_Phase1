def supprimer_double(liste):
    liste_sans_double = list(set(liste))
    return liste_sans_double

liste = [1, 2, 3, 2, 4, 5, 1, 3]
liste_sans_double = supprimer_double(liste)
print("Liste originale :", liste)
print("Liste sans double :", liste_sans_double)