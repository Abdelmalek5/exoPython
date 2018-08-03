#depuis la biblio random on importe la formule ( fonction ) randrange
#qui permet de recuperer un chiffre aleatoire 
from random import randrange

#exemple 1 
#je cree une variable phrase qui contient la chaine de caractere " Bonjour a tous "
phrase = "Bonjour a tous !"

#la boucle for permet de parcourir la phrase en recuperant chaque lettre
#demander et la stocker dans lettre
for lettre in phrase:
    #on compare la lettre recuperer avec la liste de voyelles
    if lettre in "aeiou":
        print(lettre)



#exemple 2 
#input permet de demander de tapez quelque chose au clavier 
#ici, un chiffre entier : int()
#on stoque la valeur tapee dans table 

table = int(input("tapez un chiffre : "))
multiple = 1
#tant que la variable multiple est plus petit ou egal a 0
while multiple <= 10:
    #on affiche la multiplication de la table choisie avec son multiplicateur
    print (table * multiple)
    #on augmente a chaque tour la variable multiple +1
    multiple = multiple + 1



#exemple 3
#on demande a randrange de nous donner un chiffre aleatoire compris en 0 et 99 ( le dernier n'est pas compris dedans )
#puis on stoque le resultat dans chiffre
chiffre = random.randrange(100)

#on cree une variable boolean ( qui contient vrai ou faux ) trouver qui vaut Faux ( False )
trouver = False

#tant que la variable trouver est egal a faux on continu la boucle 
while trouver == False :
    a = int(input("Entrez un chiffre : "))
    if a < chiffre:
        print("le chiffre est plus grand")
    elif a > chiffre:
        print("le chiffre est plus petit")
    else:
        print("Bravo !")
        #si on a trouver, il faut penser a changer la valeur de notre "FLAG"
        # trouver donc de notre variable qui passe a Vrai ( True ) 
        trouver = True
