"""
Auteur:Fayçal Chena
Date : 26 mars 2020
Consignes :
Écrire un programme qui lit 3 nombres entiers, et qui,
si au moins deux d’entre eux ont la même valeur,
imprime cette valeur (le programme n’imprime rien dans le cas contraire).

"""

number_1 = print(int(input("Indiquer le premier nombre:")))
number_2 = print(int(input("Indiquer le second nombre:")))
number_3 = print(int(input("Indiquer le troisième nombre:")))

if number_1 == number_2:
    print(number_1)
elif number_1 == number_3:
    print(number_1)
elif number_2 == number_3:
    print(number_2)
