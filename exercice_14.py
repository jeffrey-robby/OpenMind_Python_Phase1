nombre_entier = int(input("Veuillez saisir un nombre entier n : "))

racine = int(nombre_entier ** 0.5)

if racine * racine == nombre_entier:
    print("est un carré parfait !")
else:
   print("n'est pas un carré parfait !")