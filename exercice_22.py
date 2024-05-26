def premier_mot(texte):
    mots = texte.split()

    if mots:
        premier_mot = mots[0]
        return premier_mot
    else:
        return None

texte = input("Entrez un texte : ")

resultat = premier_mot(texte)

if resultat:
    print("Le premier mot du texte est :", resultat)