chaine_de_caractere = input("Veuillez saisir une chaîne de caractères : ")

mots = chaine_de_caractere.split()

if len(mots) >= 2:
    mots[0], mots[-1] = mots[-1], mots[0]
    chaine_modifiee = " ".join(mots)
else:
    chaine_modifiee = chaine_de_caractere

print("Chaîne modifiée :", chaine_modifiee)