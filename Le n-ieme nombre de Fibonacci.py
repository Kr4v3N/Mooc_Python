# La suite de Fibonacci (1)
# Si l’on veut écrire les n premiers termes de la suite,
# il suffit de les calculer un à un et de les afficher
n = int(input('nombre de termes à calculer de la suite de Fibonacci : '))

"""
une façon classique de calculer un terme suivant est d’avoir deux variables, 
que l’on nomme par exemple prec et succ, qui vont contenir l’avant-dernier et 
le dernier terme calculés.
"""
prec = 0
succ = 1
print(prec, end=" ")
print(succ, end=" ")
for i in range(n - 2):
    """
    À chaque itération, il faut calculer le terme suivant mais aussi conserver l’avant-dernier, 
    c’est-à-dire celui qui était dans succ pour nous permettre de continuer.
    """
    prec, succ = succ, prec + succ
    print(succ, end=" ")
print()

"""
Le range(n-2) est dû au fait que les 2 premiers termes ont déjà été imprimés 
et qu’il en reste donc n-2 à calculer.
Notons aussi l'explicitation de l'argument nommé end dans les print, 
pour imprimer les résultats sur la même ligne (avec end = " ", 
chaque print est séparé par une espace), et le dernier print() 
permet de passer à la ligne après avoir imprimé la dernière valeur.
"""

# La suite de Fibonacci (2)
"""
on ne sait pas a priori combien d’itérations devront être effectuées. 
Dans ce cas, un while est la bonne instruction à utiliser.
"""
n = int(input('Borne supérieur à ne pas dépasser pour calculer la suite de Fibonacci : '))
prec = 0
succ = 1
print(prec, end=" ")
while succ < n:
    print(succ, end=" ")
    prec, succ = succ, prec + succ
print()

"""
Notons qu’ici en plus d’utiliser un while, succ est imprimé juste après le test 
(condition de continuation du while) pour s’assurer qu’il faut effectivement l’imprimer.
"""


def fibo(n):
    """calcule le n-ième nombre de Fibonacci, avec : n de type int """

    if n == 1 or n == 2:
        return 1
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


for i in range(1, 21):
    print(fibo(i))
