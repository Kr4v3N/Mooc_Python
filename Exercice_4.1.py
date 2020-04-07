"""
Auteur:Fayçal Chena
Date : 07 avril 2020
Consignes :
Écrire une fonction deux_egaux(a, b, c) qui reçoit trois nombres en paramètre
et qui renvoie la valeur booléenne True si au moins deux de ces nombres
ont la même valeur, et la valeur booléenne False sinon.
Ensuite, écrire un programme qui lit trois données de type int, x, y et z,
et affiche le résultat de l’exécution de deux_egaux(x, y, z).
"""


def deux_egaux(a, b, c):
    if a == b or b == c or c == a:
        return True
    else:
        return False


x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))

print(deux_egaux(x, y, z))
