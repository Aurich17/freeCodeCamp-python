x = 1

while x < 3:
    #Preguntas al usuario
    animal = input("Dime un animal ---> ")
    nombre = input("Dame un nombre ---> ")
    accion = input("Dime una acccion ---> ")
    lugar = input("Dime una lugar ---> ")
    grupoMusical = input("Dime una grupoMusical ---> ")

    #Contando historia
    print(f""" HISTORIA RANDOM
    {nombre} se levanto por la mañana como un dia normal, cuando de la nada
    aparecio un {animal} en {lugar}, el cual estaba acompañado 
    de {grupoMusical}, los cuales se pusieron a {accion}""")

    x += 1