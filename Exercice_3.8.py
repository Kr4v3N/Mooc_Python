"""
Auteur: Fayçal Chena
Date : 26 mars 2020
Consignes:
Écrire un programme qui lit :
la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),
la longueur de l’arête du polyèdre,
et qui imprime le volume du polyèdre correspondant.
Si la lettre lue ne fait pas partie des cinq initiales,
le programme imprime le message "Polyèdre non connu".
"""
polyedres = str(input())
polyedres_len = float(input())

if polyedres == "T":
    print((1.41421356237 / 12) * (polyedres_len ** 3))

if polyedres == "C":
    print(polyedres_len ** 3)

if polyedres == "O":
    print((1.41421356237 / 3) * (polyedres_len ** 3))

if polyedres == "D":
    print(((15 + 15.6524758425) / 4) * (polyedres_len ** 3))

if polyedres == "I":
    print((5 * (3 + 2.2360679775) / 12) * (polyedres_len ** 3))

if polyedres != str("T") and polyedres != str("C") and polyedres != str("O") \
        and polyedres != str("D") and polyedres != str("I"):
    print("Polyèdre non connu")
