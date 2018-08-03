import math
from nosFonctions import *

#on utulise notre fonction qui permet de recuperer un chiffre entier tapez au clavier 
a = tapezEntier()
b = tapezEntier()
c = tapezEntier()

#on sait que pour resoudre l'equation on doit trouver le delta ( google )
delta = (b*b) - 4*a*c #formule trouver sur google 
print("le delta = ", delta)

if delta > 0 :
    print ("2 valeurs possible.")
    #si delta est plus grand que 0 on sait que l'on deux reponse
    #et qu'il faut utuliser les formule suivante 
    x1 = (-b + math.sqrt(delta)) / (2*a)#math.sqrt c'est la racine carre 
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("x1 = ",x1," x2= ",x2)

elif delta == 0 :
    print ("1 valeur possible")
    #si delta est egal a 0 on sait que l'on a une reponse
    #et qu'il faut utuliser les formule suivante 
    x1 = -b  / (2*a)

    print("x = ",x1)

else:
    print("pas de réponse.")
    