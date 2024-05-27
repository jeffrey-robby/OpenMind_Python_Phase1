chaine_de_caractere_1 = input("Veuillez saisir la première chaîne de caractères : ")
chaine_de_caractere_2 = input("Veuillez saisir la deuxième chaîne de caractères : ")

mots_chaine_de_caractere1 = set(chaine_de_caractere_1.split())
mots_chaine_de_caractere2 = set(chaine_de_caractere_2.split())

mots_en_communs = list(mots_chaine_de_caractere1.intersection(mots_chaine_de_caractere2))

print(mots_en_communs)