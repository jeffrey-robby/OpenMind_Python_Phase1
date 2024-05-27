def liste_vide(liste):
    if len(liste) == 0:
        return True
    else:
        return False

def chaine_vide(chaine):
    if len(chaine) == 0:
        return True
    else:
        return False

liste = [1, 2, 3, 4, 5]
if  liste_vide(liste):
    print("La liste est vide.")
else:
    print("La liste n'est pas vide.")

chaine_de_caractere = "Bonjour, OpenMind!"
if  chaine_vide(chaine_de_caractere):
    print("La chaîne de caractères est vide.")
else:
    print("La chaîne de caractères n'est pas vide.")