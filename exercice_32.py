def permutations_liste(liste):
    if len(liste) <= 1:
        return [liste]
    
    permutations = []  
    
    for i in range(len(liste)):
        element = liste[i]
        restant = liste[:i] + liste[i+1:]  
        
        permutations_restantes = permutations_liste(restant)
        
        for permutation in permutations_restantes:
            permutations.append([element] + permutation)
    
    return permutations

liste_de_nombres = [1, 2, 3]
resultat = permutations_liste(liste_de_nombres)

print("Liste originale :", liste_de_nombres)
print("Permutations possibles :", resultat)