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


"""
Calcul du plus grand commun diviseur de deux nombres entiers positifs.
"""
x = int(input("x= "))
y = int(input("y= "))
while y > 0:
    x, y = y, x % y
    print(x, y)
print("pgcd= ", x)


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

# Une instruction for peut être réécrite en un while.
# l’exemple ci-dessous :
for i in range(10):
    print(i)

# peut être écrit comme suit :

i = 0
while i < 10:
    print(i)


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
