chaine_de_caractere = input("Veuillez saisir une chaîne de caractères : ")

mots = chaine_de_caractere.split()
chaine_sans_espaces_multiples = " ".join(mots)

print("Chaîne sans espaces multiples :", chaine_sans_espaces_multiples)