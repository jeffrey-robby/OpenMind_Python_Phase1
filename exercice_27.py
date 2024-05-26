def calcule_somme(liste):
    somme = 0
    for nombre in liste:
        somme = nombre + somme
    return somme

def multiplication_liste(liste):
    produit = 1
    for nombre in liste:
        produit = nombre * produit
    return produit

liste_des_nombres = [1, 2, 3, 4, 5]
somme = calcule_somme(liste_des_nombres)
print("La somme des éléments de la liste est :", somme)

produit = multiplication_liste(liste_des_nombres)
print("Le produit des éléments de la liste est :", produit)