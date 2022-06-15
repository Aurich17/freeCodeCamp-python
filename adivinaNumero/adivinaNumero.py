from random import randrange

num = randrange(1, 50)
contador = 1

while True:
    usuario = int(input("¿Adivina el número secreto en el rango del 1 al 50? ---> "))
    if usuario == num:
        print(f"Felicidades, como sabias que el número secreto era {num} y solo te tomo {contador} intentos")
        break
    elif usuario > num:
        contador += 1
        print(f"Bajale mas")
    elif usuario < num:
        contador += 1
        print(f"Subele mas")
    else:
        print(f"Ingresa un numero valido")