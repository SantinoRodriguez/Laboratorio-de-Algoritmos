import json

with open("Numero_Favorito.json", "r") as Archivo:
    Contenido = Archivo.read()
    NumeroFavorito = json.loads(Contenido)

print(f"¡Sé cuál es tu número favorito! Es {NumeroFavorito}.")
