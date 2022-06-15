from random import choice

while True:
    manos = ["piedra", "papel", "tijera"]
    mano = choice(manos)
    print(f"""
    ---OPCIONES---
    1.Piedra
    2.Papel
    3.Tijera
    4.Salir del Juego""")
    usuario = int(input("Escribe el numero de tu elección ----> "))
    #Verificando el resultado
    if usuario == 4:
        print("Fin del juego")
        break
    else:
        usuarioMano = manos[usuario-1]
        if usuarioMano == mano:
            print(f"Haz empatado, ambos han sacado {mano}")
        elif usuarioMano == "piedra" and mano == "tijera":
            print(f"Felicidades tu ganas haz sacado {usuarioMano} y el {mano}!!")
        elif usuarioMano == "piedra" and mano == "papel":
            print(f"Lo sentimos tu pierdes")
        elif usuarioMano == "papel" and mano == "tijera":
            print(f"Lo sentimos tu pierdes")
        elif usuarioMano == "papel" and mano == "piedra":
            print(f"Felicidades tu ganas haz sacado {usuarioMano} y el {mano}!!")
        elif usuarioMano == "tijera" and mano == "papel":
            print(f"Felicidades tu ganas haz sacado {usuarioMano} y el {mano}!!")
        elif usuarioMano == "tijera" and mano == "piedra":
            print(f"Lo sentimos tu pierdes")
 