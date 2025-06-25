print("Ingresá 'salir' en cualquier momento para terminar.")

with open("guest_book.txt", "a") as archivo:
    while True:
        Nombre = input("Por favor, ingresá tu nombre: ")

        if Nombre.lower() == 'salir':
            break

        archivo.write(Nombre + "\n")
        print(f"Hola, {Nombre}. Tu nombre fue agregado al libro de invitados.")
