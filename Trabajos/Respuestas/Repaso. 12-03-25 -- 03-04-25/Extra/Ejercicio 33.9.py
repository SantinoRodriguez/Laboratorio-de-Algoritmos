import json
import os

ArchivoNombre = "numero_favorito.json"

if os.path.exists(ArchivoNombre):
    with open(ArchivoNombre, "r") as Archivo:
        Contenido = Archivo.read()
        if Contenido:
            NumeroFavorito = json.loads(Contenido)
            print(f"¡Sé cuál es tu número favorito! Es {NumeroFavorito}.")
        else:
            NumeroFavorito = input("¿Cuál es tu número favorito? ")
            with open(ArchivoNombre, "w") as Archivo:
                ContenidoJSON = json.dumps(NumeroFavorito)
                Archivo.write(ContenidoJSON)
else:
    NumeroFavorito = input("¿Cuál es tu número favorito? ")
    with open(ArchivoNombre, "w") as Archivo:
        ContenidoJSON = json.dumps(NumeroFavorito)
        Archivo.write(ContenidoJSON)
