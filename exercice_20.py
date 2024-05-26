chaine_de_caractere = input("Entrez une chaîne de caractères : ")

if len(chaine_de_caractere ) >= 2:
    premier_caractere = chaine_de_caractere [0]
    dernier_caractere = chaine_de_caractere [-1]

    nouvelle_chaine = dernier_caractere + chaine_de_caractere [1:-1] + premier_caractere

    print("Chaîne modifiée :", nouvelle_chaine)
else:
    print("La chaîne doit contenir au moins deux caractères.")