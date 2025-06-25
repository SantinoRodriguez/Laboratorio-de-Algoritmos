import random
Nombres = ["Juan", "Ana", "Luis", "Maria", "Pedro"]
Diccionario = {Nombre: random.randint(1, 100) for Nombre in Nombres}

for Nombre in Diccionario:
    print(f"{Nombre}: {Diccionario[Nombre]}")
