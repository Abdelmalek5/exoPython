choix = int(input("Tapez 1 pour C->F et 2 pour F->C"))


if choix == 1:
    #on convertit de celcius en farenheit 
    c= int(input("Tapez une temperature en C°"))
    farenheit = (c*1.8)+32 #formule trouver sur google pour convertir temperature
    print(farenheit)

elif choix == 2:
    #on convertit de farenheit en celcius
    f= int(input("Tapez une temperature en F°"))
    celcius = (f-32)/1.8
    print(celcius)