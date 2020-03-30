"""
Auteur: Fayçal Chena
Date : 25 mars 2020
Petit jeu de devinette (version 1)
Consignes : le programme :
    — choisit aléatoirement un nombre entre 0 et 5 sans en afficher la valeur (et donc sans que l’utilisateur connaisse cette valeur)
    et le place dans la variable secret ;
    — demande à l’utilisateur de deviner la valeur choisie ;
    — affiche "gagné !" si l’utilisateur trouve la bonne réponse et
    — affiche "perdu ! La valeur était " suivi de la valeur de secret dans le cas contraire.
"""

import random

secret = random.randint(0, 5)
essai = int(input("Deviner la valeur choisie entre 0 et 5: "))

if secret == essai:
    print("Bravo ! c'est la bonne valeur :)")
else:
    print("perdu ! la valeur était", secret)

print("Au revoir !")


