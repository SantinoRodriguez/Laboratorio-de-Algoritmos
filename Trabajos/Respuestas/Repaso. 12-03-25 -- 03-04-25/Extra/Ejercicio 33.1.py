Nombre = input("Por favor, ingresá tu nombre: ")
with open("guest.txt", "w") as archivo:
    archivo.write(Nombre)

print("Tu nombre ha sido guardado en guest.txt.")
