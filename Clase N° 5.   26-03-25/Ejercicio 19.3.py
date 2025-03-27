Maxingredientes = 10
Contador = 0
while Contador < Maxingredientes:
    Ingrediente = input("Ingresa un Ingrediente Para Tu Pizza (Escribe 'salir' Para Terminar): ")
    if Ingrediente.lower() == "salir":
        break
    print(f"¡Vas a Agregar {Ingrediente.capitalize()} a Tu Pizza!")
    Contador += 1
if Contador == Maxingredientes:
    print("Has Alcanzado el Limite de Ingredientes")
print("¡Listo! Tu Pizza Está Lista Con Los Ingredientes Que Elegiste.")