"""
Auteur:Fayçal Chena
Date : 07 avril 2020
Consignes :
Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif
n et qui renvoie True si n est un nombre premier, et False sinon.
Ensuite, écrire un programme qui lit une valeur entière x et affiche,
grâce à des appels à la fonction premier, tous les nombres premiers
strictement inférieurs à x, chacun sur sa propre ligne.
"""
import math

n = int(input())

def premier(n):
    """ renvoie vrai si n est un nombre premier"""

    i = 2
    while i * i <= n and n % i != 0:
        i = i + 1
    if i * i > n > 1:
        return True
    else:
        return False

print(premier(n))

# code principal
print("liste des nombres premiers jusqu'à {} : ".format(n))
for i in range(n):
    if premier(i):
        print(i)

