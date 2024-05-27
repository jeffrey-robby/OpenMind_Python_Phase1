def palindrome(mot):
    mot_inverse = mot[::-1]  

    if mot == mot_inverse:
        return True
    else:
        return False

mot = input("Veuillez saisir un mot : ")

if  palindrome(mot):
    print("Le mot", mot, "est un palindrome.")
else:
    print("Le mot", mot, "n'est pas un palindrome.")