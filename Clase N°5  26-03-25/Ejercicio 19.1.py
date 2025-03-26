while True:
    Ingrediente = input("Ingresa un Ingrediente Para Tu Pizza (Wscribe 'salir' Para Terminar): ")
    if Ingrediente.lower() == "salir":
        break
    print(f"¡Vas a Agregar {Ingrediente.capitalize()} a Tu Pizza!")
print("¡Listo! Tu Pizza Está Lista Con Los Ingredientes Que Elegiste.")
