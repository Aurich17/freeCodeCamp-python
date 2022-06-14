def parOimpar(num):
    return num%2
while True:
    num = int(input("¿En qué número estas pensando? ----> "))
    val = parOimpar(num)
    if val == 0:
        print("¡Es un numero par! ¿Puedes añadir otro?")
    else:
        print("¡Es un numero impar! ¿Puedes añadir otro?")

