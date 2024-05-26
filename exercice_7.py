premier_nombre = float(input("Veuillez saisir le premier nombre x : "))
deuxieme_nombre = float(input("Veuillez saisir le deuxième nombre y : "))
troisieme_nombre = float(input("Veuillez saisir le troisième nombre z : "))

maximum = premier_nombre

if deuxieme_nombre > maximum:
    maximum = deuxieme_nombre

if troisieme_nombre > maximum:
    maximum = troisieme_nombre

print("Le maximum est :", maximum)