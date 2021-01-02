"""
Auteur:Fayçal Chena
Date : 01 avril 2020
Consignes :
Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer.
Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :
si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;
si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire
qui sera terminée par le caractère "F" signifiant que la liste est terminée.
"""

somme = 0
data = 0

n = int(input("Nombre de valeur à saisir: "))

if n > 0:
    while n > 0:
        n -= 1
        data = int(input("Donner une valeur: "))
        somme += data
    print(somme)
else:
    while n < 0:
        data = input("Donner une valeur: ")
        if data != 'F':
            n -= 1
            somme += int(data)
            data = int(data)
        else:
            break
    print(somme)

