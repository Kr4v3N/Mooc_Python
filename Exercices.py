"""
Aller sur la lune c'est facile !
il suffit de plier une feuille 42 fois et de se mettre dessus !
"""
DISTANCE = 3.844e8
nombre_pliages = 0
epaisseur = 0.0001

while epaisseur < DISTANCE:
    nombre_pliages = nombre_pliages + 1
    epaisseur = 2 * epaisseur
print("Nombre de pliages nécessaires :", nombre_pliages)

---------------------------------------------------------------------

"""
Calcul du plus grand commun diviseur de deux nombres entiers positifs.
"""

x = int(input("x= "))
y = int(input("y= "))
while y > 0:
    x, y = y, x % y
    print(x, y)
print("pgcd= ", x)

----------------------------------------------------------------------
"""
La conjecture de Syracuse
"""

# Le nombre n est lu sur input :
n = int(input("Valeur du nombre n dont on veut tester la conjecture : "))

# Calculer la valeur suivante peut se faire avec une instruction if.
if n % 2 == 0:  # si un nombre entier modulo 2 vaut 0, il est pair
    n = n // 2
else:    # cas où le nombre est impair
    n = 3 * n + 1
# Enfin pour tester si la suite satisfait la conjecture, il faut continuer à
# calculer de nouvelles valeurs jusqu’à ce que n vaille 1 :
while n != 1:
   print(n)
   if n % 2 == 0:
       n = n//2
   else:
       n = n*3+1
print(n)  # imprime 1

------------------------------------------------------------------------

""" trace une étoile à n côtés, si elle peut l'être sans lever la plume"""

import turtle
from math import gcd  # fonction du module math qui calcule le pgcd de 2 nombres

LONGUEUR = 100  # taille de chaque segment de l'étoile

n = int(input("Combien de branches désirez-vous ? : "))
inc = (n - 1) // 2
while gcd(n, inc) > 1:
    inc = inc - 1
if inc == 1:
    print("Impossible de dessiner une étoile à", n, "branches en un tenant")
else:
    angle = 180 - (n - 2 * inc) * 180 / n
    for i in range(n):
        turtle.forward(LONGUEUR)
        turtle.left(angle)
    turtle.done()

------------------------------------------------------------------------------
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
----------------------------------------------------------------------------------

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

------------------------------------------------------------------

# Une instruction for peut être réécrite en un while.

# l’exemple ci-dessous :
for i in range(10):
    print(i)

# peut être écrit comme suit :

i = 0
while i < 10:
    print(i)

------------------------------------------------------------------------

""" auteur: Thierry Massart
   date : 9 avril 2018 
   but du programme : trace avec turtle les contours d’un pavé hexagonal
"""
import turtle

for i in range(3):  # à chaque itération, trace un losange
    angle = 120
    for j in range(4):  # à chaque itération, trace un segment
        turtle.forward(100)
        turtle.left(angle)
        angle = 180 - angle
    turtle.right(120)
turtle.hideturtle()
turtle.done()
