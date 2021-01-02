"""
Auteur:Fayçal Chena
Date : 07 avril 2020
Consignes :
 vous allez dans un premier temps écrire une fonction soleil_leve qui, pour un soleil
 particulier, reçoit trois valeurs entières en argument pour la planète :
     - l'heure de lever du soleil (entre 0 et 23)
     - l'heure du coucher du soleil (entre 0 et 23)
     - l'heure actuelle (entre 0 et 23)
et qui renvoie une valeur booléenne vraie si le soleil est levé sur la planète
à l'heure donnée en troisième argument et fausse, s'il est couché.
"""


def soleil_leve(leve, couche, actuelle):
    cas1 = leve == couche == 0
    cas2 = leve <= actuelle < couche
    cas3 = couche < leve and (actuelle < couche or leve <= actuelle)
    return cas1 or cas2 or cas3


lE1515 = int(input())
cE1515 = int(input())
lE666 = int(input())
cE666 = int(input())

for actuelle in range(24):
    if soleil_leve(lE1515, cE1515, actuelle) or soleil_leve(lE666, cE666, actuelle):
        print(actuelle)
    else:
        print(actuelle, "*")
