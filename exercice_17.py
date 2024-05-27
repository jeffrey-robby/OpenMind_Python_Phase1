chaine_de_caractere = input("Veuillez saisir une chaîne de caractères : ")

occurrences = {}

for caractere in chaine_de_caractere:
    if caractere in occurrences:
        occurrences[caractere] = 1 + occurrences[caractere]
    else:
        occurrences[caractere] = 1

for caractere in occurrences:
    nb_occurrences = occurrences[nb_occurrences]
    print("Le caractère :", caractere, "figure", nb_occurrences, "fois dans la chaîne", chaine_de_caractere )