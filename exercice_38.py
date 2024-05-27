chaine_de_cractere = input("Veuillez saisir une chaîne de caractères : ")

mots = chaine_de_cractere.split()

mot_le_plus_long = ""

for mot in mots:
    if len(mot) > len(mot_le_plus_long):
        mot_le_plus_long = mot

print("Mot le plus long :", mot_le_plus_long)