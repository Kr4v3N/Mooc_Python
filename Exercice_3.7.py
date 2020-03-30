"""
Auteur: Fayçal Chena
Date : 26 mars 2020
Consignes:
Écrire un programme qui aide le croupier à déterminer la somme que le casino doit
donner au joueur.
Le programme lira, dans l’ordre, deux nombres entiers en entrée :
le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas),
et le numéro issu du tirage (nombre entre 0 et 12).
Le programme affichera alors le montant gagné par le joueur.
"""

bet = int(input("Votre pari: "))
result = int(input("Le résultat: "))

if bet == result:
    print(int(10 * 12))

elif result % 2 == 0 and bet == 13:
    print(int(10 * 2))

elif result % 2 != 0 and bet == 14:
    print(int(10 * 2))

elif result == 1 and bet == 15:
    print(int(10 * 2))

elif result == 3 and bet == 15:
    print(int(10 * 2))

elif result == 5 and bet == 15:
    print(int(10 * 2))

elif result == 7 and bet == 15:
    print(int(10 * 2))

elif result == 9 and bet == 15:
    print(int(10 * 2))

elif result == 12 and bet == 15:
    print(int(10 * 2))

elif result == 2 and bet == 16:
    print(int(10 * 2))

elif result == 4 and bet == 16:
    print(int(10 * 2))

elif result == 6 and bet == 16:
    print(int(10 * 2))

elif result == 8 and bet == 16:
    print(int(10 * 2))

elif result == 10 and bet == 16:
    print(int(10 * 2))

elif result == 11 and bet == 16:
    print(int(10 * 2))

else:
    print(int(0))


