usuario = input("Ingresa una palabra ---> ").upper()

palabraN = []
palabraV = []

#Agregando las letras de la palabra a la lista
for i in range(len(usuario)):
    palabraN.append(usuario[i])

x = 1
for i in range(len(usuario)):
    palabraV.append(palabraN[len(usuario)- x])
    x+=1

if palabraV == palabraN:
    print("Felicidades es una palabra palindroma")
else:
    print("No es una palabra palindroma")