import json

ArchivoNombre = "persona_info.json"

Nombre = input("¿Cómo te llamás? ")
Edad = input("¿Cuántos años tenés? ")
Ciudad = input("¿En qué ciudad vivís? ")

DatosPersona = {
    "Nombre": Nombre,
    "Edad": Edad,
    "Ciudad": Ciudad
}

with open(ArchivoNombre, "w") as Archivo:
    ContenidoJSON = json.dumps(DatosPersona)
    Archivo.write(ContenidoJSON)

with open(ArchivoNombre, "r") as Archivo:
    ContenidoLeido = Archivo.read()
    DatosRecuperados = json.loads(ContenidoLeido)

print(f"\nRecuerdo que te llamás {DatosRecuperados['Nombre']}, "
      f"tenés {DatosRecuperados['Edad']} años "
      f"y vivís en {DatosRecuperados['Ciudad']}.")
