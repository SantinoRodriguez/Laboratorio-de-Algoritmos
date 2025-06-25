import json

NumeroFavorito = input("¿Cuál es tu número favorito? ")

with open("Numero_Favorito.json", "w") as Archivo:
    ContenidoJSON = json.dumps(NumeroFavorito)
    Archivo.write(ContenidoJSON)
