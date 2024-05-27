def obtenir_extension(nom_du_fichier):
    derniere_parties = nom_du_fichier.split(".")

    if len(derniere_parties) > 1:
        extension = derniere_parties[-1]
        return "." + extension
    
nom_fichier = input("Veuillez saisir le nom d'un fichier : ")

resultat = obtenir_extension(nom_fichier)

if resultat:
    print("L'extension du fichier est :", resultat)