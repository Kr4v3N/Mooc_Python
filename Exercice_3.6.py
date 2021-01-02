"""
Auteur: Fayçal Chena
Date : 26 mars 2020
Consignes :
Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b}
(la racine carrée du produit de a par b) de deux nombres positifs a
et b de type float lus en entrée.
Si au moins un de ces nombres est strictement négatif, le programme
imprime le texte « Erreur ».
"""
import math

number_1 = float(input("1 chiffre : "))
number_2 = float(input("2ème chiffre: "))

if number_2 < 0 or number_1 < 0:
    print("Erreur")
else:
    moyenne_geo = math.sqrt(number_1 * number_2)
    print(moyenne_geo)
