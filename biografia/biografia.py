while True:
    nombre = input("¿Cual es tu nombre? ---> ")
    if nombre.isalpha():
        nacimiento = input("¿Cuando naciste? ---> ")
        direccion = input("¿Cual es tu direccion? ---> ")
        metas = input("¿Cuales son tus metas? ---> ")
        #Imprimiendo biografia
        print(f"""
        Nombre: {nombre}
        Nacimiento: {nacimiento}
        Direccion: {direccion}
        Metas: {metas}""")
        break
    else:
        print("Escribe un nombre valido")