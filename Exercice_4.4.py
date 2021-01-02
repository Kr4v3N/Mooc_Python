"""
Auteur:Fayçal Chena
Date : 07 avril 2020
Consignes :
Écrire une fonction fibo(n) qui reçoit un nombre entier n
et qui renvoie la valeur du nombre de Fibonacci F_n.
On rappelle que :
F_0 vaut 0 ;
F_1 vaut 1 ;
F_{i + 1} vaut F_i + F_{i-1} pour i > 0 ;
F_i vaut None pour i < 0.
Ensuite, écrire un programme qui lit une valeur entière
strictement positive x et affiche le résultat de fibo(i)
pour i allant de 0 compris à x non compris,
avec chaque valeur sur sa propre ligne.
"""


def fibo(n):
    """calcule le n-ième nombre de Fibonacci, avec : n de type int """

    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return None
    else:
        precedent = 1
        courant = 1
        for j in range(n - 2):
            res = precedent + courant
            precedent = courant
            courant = res
            '''
            precedent, courant = courant, precedent + courant
            '''
        return courant


x = int(input("Valeur de x : "))
for i in range(0, x):
    print(fibo(i))
