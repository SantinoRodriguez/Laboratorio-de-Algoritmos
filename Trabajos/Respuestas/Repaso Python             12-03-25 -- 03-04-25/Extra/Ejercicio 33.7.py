RutaArchivo = "Libro.txt"

try:
    with open(RutaArchivo, encoding="utf-8") as Archivo:
        Contenido = Archivo.read().lower()

        ConteoThe = Contenido.count("the")
        ConteoTheEspacio = Contenido.count("the ")

        print(f"Apariciones de 'the': {ConteoThe}")
        print(f"Apariciones de 'the ': {ConteoTheEspacio}")

except FileNotFoundError:
    pass
