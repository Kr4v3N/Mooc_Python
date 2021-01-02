"""
Auteur:Fayçal Chena
Date : 03 avril 2020
Consignes :
Écrire un programme qui teste si, pour une configuration donnée,
un écureuil va ou non atteindre la noisette. Il reçoit deux valeurs entières en entrée,
une valeur saut et une valeur position_cible, toutes deux entre 1 et 99.
"""

saut = int(input())
position_courante = saut
cible = int(input())

while True:
    if position_courante != cible:
        print(position_courante)
        position_courante = (position_courante + saut) % 100
    else:
        print("Cible atteinte")
        break
    if position_courante == 0:
        print(position_courante)
        position_courante = (position_courante + saut) % 100
        print("Pas trouvé")
        break
