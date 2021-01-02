"""
Auteur:Fayçal Chena
Date : 02 avril 2020
Consignes :
Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret)
compris entre 0 et 100. Ensuite, le joueur doit deviner ce nombre en utilisant
le moins d’essais possible.
"""

import random

NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
print("le nombre secret est", secret)
QUESTION = "Deviner la valeur choisie entre 0 et 100: "

n = int(input(QUESTION))
essais = 1

while n != secret:

    if essais < 6:

        if n < secret:
            print('Trop petit')
        else:
            print('Trop grand')
        essais += 1
        n = int(input())
    else:
        print('Perdu ! le secret était {}'.format(secret))
        exit()

print('Gagné en {} essais !'.format(essais))
