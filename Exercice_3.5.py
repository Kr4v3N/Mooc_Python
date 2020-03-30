"""
Auteur: Fayçal Chena
Date : 26 mars 2020
Consignes :
Écrire un programme qui lit en entrée deux nombres entiers
strictement positifs, et qui vérifie qu’aucun des deux n’est
un diviseur de l’autre.
"""

number_1 = int(input())
number_2 = int(input())

if number_1 % number_2 == 0:
    print("False")
else:
    print("True")
