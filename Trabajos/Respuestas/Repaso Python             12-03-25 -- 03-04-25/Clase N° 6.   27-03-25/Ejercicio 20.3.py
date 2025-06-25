Destinos = []
while True:
    Destino = input("¿Cual Es Tu Destino de Vacaciones Soñado?: ")
    Destinos.append(Destino.capitalize())
    for i in Destinos:
        print(f"- {i}")