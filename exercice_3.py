premier_nombre = float(input("Veuillez saisir le premier nombre a : "))
deuxieme_nombre = float(input("Veuillez saisir le deuxième nombre b : "))

if premier_nombre > deuxieme_nombre:
    maximum = premier_nombre
else:
    maximum = deuxieme_nombre

print("Le maximum entre",premier_nombre, "et", deuxieme_nombre, "est", maximum)