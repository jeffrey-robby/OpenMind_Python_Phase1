nombre_entier = int(input("Veuillez saisir un nombre entier n : "))

if nombre_entier  < 2:
    print("n'est pas un nombre premier !")
else:
    est_premier = True
    for i in range(2, nombre_entier ):
        if nombre_entier  % i == 0:
            est_premier = False
            break

    if est_premier:
        print("est un nombre premier !")
    else: print("n'est pas un nombre premier !")