#on defini nos fonctions chaque fonction comprend :
#def nomDefonction () :
#si on a besoin que notre fonction nous donne une reponse,
#on met un "return" + ce que l'on demande ( variable )
def tapezLettre ():
    boite = input("tapez les characteres")
    #ici on demande que l'on nous renvois la valeur contenu
    #dans boite donc ce que l'on a tapez au clavier 
    return boite

def tapezEntier ():
    boite = int(input("tapez un chiffre entier "))
    return boite

def tapezFloat ():
    boite = float(input("tapez un chiffre à virgule"))
    return boite



def tableMultiplication ( table ):
    multiplicateur = 1
    while multiplicateur <= 10:
        print (table * multiplicateur)
        multiplicateur = multiplicateur + 1

