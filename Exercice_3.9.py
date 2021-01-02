"""
Auteur:Fayçal Chena
Date : 28 mars 2020
Consignes :
Écrire un programme qui demande à l’utilisateur combien de plis de papier
sont nécessaires pour se rendre sur la Lune, et pose la question
tant que l’utilisateur n’a pas saisi la bonne réponse.

"""

reponse = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))

while reponse != 42:
    print("Mauvaise réponse.")
    reponse = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))

print("Bravo !")
