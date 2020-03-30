"""
Auteur:Fayçal Chena
Date : 29 mars 2020
Consignes :
Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer.
Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :
si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;
si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire
qui sera terminée par le caractère "F" signifiant que la liste est terminée.
"""

data = int(input("Donner une chiffre qui determinera la suite: "))

for i in range(data):
    print()
