Lista = []
for i in range(0,4):
    Elemento = input(f"Escoga Un Elemento Para Agragar En La Posicion {i + 1}: ")
    Lista.append(Elemento)
print(" - ".join(Lista)) # Deja lo que esta en las comilla entre los elementos al printear