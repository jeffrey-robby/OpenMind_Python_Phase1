chaine_de_caractere  = input("Entrez une chaîne de caractères : ")
positions = []

for i in range(len(chaine_de_caractere )):
    if chaine_de_caractere [i] == 'a':
        positions = positions + [i + 1]  

if positions:
    for position in positions:
        print("La lettre 'a' se trouve à la position :", position)
else:
    print("La lettre 'a' n'a pas été trouvée dans la chaîne.")