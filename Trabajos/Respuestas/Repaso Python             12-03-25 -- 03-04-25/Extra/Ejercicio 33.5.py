with open("gatos.txt", "w") as ArchivoGatos:
    ArchivoGatos.write("Milo\n")
    ArchivoGatos.write("Luna\n")
    ArchivoGatos.write("Simba\n")

with open("perros.txt", "w") as ArchivoPerros:
    ArchivoPerros.write("Firulais\n")
    ArchivoPerros.write("Toby\n")
    ArchivoPerros.write("Lola\n")


def LeerArchivos(Nombre):
    try:
        with open(Nombre, "r") as Archivo:
            Contenido = Archivo.read()
            print(f"Contenido de {Nombre}:\n{Contenido}")
    except FileNotFoundError:
        print(
            f"El archivo '{Nombre}' no fue encontrado. Por favor, verifique su ubicación.")


LeerArchivos("gatos.txt")
LeerArchivos("perros.txt")
