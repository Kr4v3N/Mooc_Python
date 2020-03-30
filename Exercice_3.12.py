"""
Auteur:Fayçal Chena
Date : 29 mars 2020
Consignes :
Écrire un programme qui lit en entrée une valeur naturelle n et
qui affiche à l’écran un triangle supérieur droit formé de X.
"""
value = int(input("Donner votre valeur : "))
t = ""

for x in range(value):
    print(t, "X" * value, sep='')
    t = t + " "
    value = value - 1