def LeerArchivos(Nombre):
    try:
        with open(Nombre, "r") as Archivo:
            Contenido = Archivo.read()
            print(f"Contenido de {Nombre}:\n{Contenido}")
    except FileNotFoundError:
        pass


LeerArchivos("gatos.txt")
LeerArchivos("perros.txt")
