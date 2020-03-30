"""
Auteur: Fayçal Chena
Date : 26 mars 2020
Écrire un programme qui teste la parité d’un nombre entier lu
sur input et imprime True si le nombre est pair,
False dans le cas contraire.
"""

number = int(input("Donner un nombre: "))

if number % 2 != 0:
    print("False")
else:
    print("True")
