x = 10
while x > 0:
    x = x - 1
    print(x)

"""
le while réalise au total 10 impressions de valeurs de x.

Effectivement ! : pour le premier test dans le while x vaut 10; à chaque itération x est décrémenté de 1 ; 
après 10 itérations complètes, x vaut 0 et l’interpréteur sort du while.

"""

x = 10
while x >= 0:
    x = x - 2
    print(x)

"""
Le while réalise au total 6 impressions de valeurs de x.

Effectivement ! Après 6 itérations complète x vaut -2 
et le test de continuation du while devient faux.

"""

x = 1
while x < 10:
    x = x + x
    print(x)

"""
Le while réalise au total 4 impressions de valeurs de x.

L’exécution d’un while correspond à une séquence test si la condition de continuation est vraie 
et si c’est le cas, exécution complète du corps de la boucle; 
ici x double à chaque itération et passe en 4 itérations de 1 à 16. 
Après la 4ème itération x vaut 16 : le test x < 10 est faux et on sort du while. 
Donc au total 4 print lors de l’exécution du while.
"""

x = 1
while x < 10:
    x = x * x
    print(x)

"""
le while boucle indéfiniment le while boucle indéfiniment.

x vaut initialement 1 et ne change jamais de valeur dans le while puisque 1*1 vaut 1. 
Donc le test x < 10 reste vrai sans arrêt (tant que le programme n’est pas interrompu par 
l’utilisateur) et ce code boucle.
"""

x = 2
while x < 10:
    x = x * x
    print(x)

"""
le while réalise au total 2 impressions de valeurs de x.

Effectivement ! Initialement x vaut 2 ; après une itération x vaut 4 (2*2) et 
après 2 itérations x vaut 16 (4*4) et on sort de la boucle while.
"""

for x in range(5):
    for y in range(4):
        print(x, y)


"""
 le for réalise au total 20 impressions du couple de valeurs x,y.
 
 Effectivement: Le code contient 2 for imbriqués. 
 La variable de contrôle du for x prend toutes les valeurs entières 
 entre 0 compris et 5 non compris soit 5 valeurs et à chaque fois 
 une itération avec le for y s’exécute et itère 4 fois (avec 4 print): 
 soit un total de 5 fois 4 = 20 print(x,y).
"""