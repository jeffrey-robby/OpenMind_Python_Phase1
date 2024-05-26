def mot_inverser(mot):
    mot_inverse = mot[::-1] 
    return mot_inverse

mot = input("Veuillez saisir un mot : ")

inverse = mot_inverser(mot)
print("L'inverse du mot", mot, "est :", inverse)