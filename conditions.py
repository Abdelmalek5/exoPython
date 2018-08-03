
boite = 5

if boite > 10 :
    print("plus grand")

elif boite < 10 :
    print("plus petit")

else:
    print("egal")


#------------------
#exemple 2

#on garde le reste de la division de 52 par 2 ( le modulo )
#avec le chiffre obtenu on le stocke dans la variable ( boite )
boite = 52 % 2

#si le contenu de la boite est agal a 0 ( zero )
#ATTENTION, double = quand on compare 2 elements
if boite == 0 :
    print("52 est un chiffre pair")