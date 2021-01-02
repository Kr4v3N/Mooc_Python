"""
Auteur:Fayçal Chena
Date : 03 avril 2020
Consignes :
Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes
une table de multiplication de taille  n x n, avec, pour i entre 1 et n,
les n premières valeurs multiples de i strictement positives sur la ième ligne.
Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris)
sont affichés sur la première ligne, les n premiers multiples de 2 sur la deuxième,
et cætera.
"""

n = int(input("Donner une valeur positif : \n"))

ligne1 = 1

for i in range(n):
    ligne2 = 1
    for j in range(n):
        print(ligne1 * ligne2, end=" ")
        ligne2 = ligne2 + 1
    ligne1 = ligne1 + 1
    print()
