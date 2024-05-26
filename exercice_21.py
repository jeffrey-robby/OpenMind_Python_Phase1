def compte_voyelles(chaine):
    liste_voyelles = "aeiouy" 
    nombre_voyelles = 0

    for caractere in chaine:
        if caractere in liste_voyelles:
            nombre_voyelles = 1 + nombre_voyelles

    return nombre_voyelles

chaine_de_caractere = input("Entrez une chaîne de caractères : ")

resultat = compte_voyelles(chaine_de_caractere)

print("La chaîne", chaine_de_caractere, "possède", resultat, "voyelles.")