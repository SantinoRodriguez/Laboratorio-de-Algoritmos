NombreArchivo = "learning_python.txt"
with open(NombreArchivo, "w") as Archivo:
    Archivo.write("En Python podés crear funciones para reutilizar código.\n")
    Archivo.write(
        "En Python podés trabajar con estructuras de datos como listas y diccionarios.\n")
    Archivo.write(
        "En Python podés manejar archivos para leer y escribir información.\n")
    Archivo.write(
        "En Python podés usar bucles para repetir tareas de forma eficiente.\n")
    Archivo.write(
        "En Python podés utilizar bibliotecas externas para ampliar funcionalidades.\n")

with open(NombreArchivo, "r") as Archivo:
    Contenido = Archivo.read()
    print("Lectura del archivo de una sola vez:")
    print(Contenido)

with open(NombreArchivo, "r") as Archivo:
    Lineas = Archivo.readlines()
    print("Lectura del archivo línea por línea:")
    for Linea in Lineas:
        print(Linea.strip())

with open(NombreArchivo, "r") as Archivo:
    print("Lectura del archivo con reemplazo de 'Python' por 'C':")
    for Linea in Archivo:
        print(Linea.replace("Python", "C").strip())
