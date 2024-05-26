def mots_commencant_par_a(texte):
    mots = texte.split()  
    mots_a = []

    for mot in mots:
        if mot.lower().startswith("a"):
            mots_a.append(mot)

    return mots_a

texte = input("Veuillez saisir un texte : ")

resultat = mots_commencant_par_a(texte)

if resultat:
    print("Les mots commençant par 'a' dans le texte sont :", resultat)
else:
    print("Aucun mot commençant par 'a' trouvé dans le texte.")