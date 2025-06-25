import json

ArchivoNombre = "usuario.json"


def ObtenerUsuarioGuardado():
    try:
        with open(ArchivoNombre, "r") as Archivo:
            NombreUsuario = json.load(Archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    else:
        return NombreUsuario


def ObtenerNuevoUsuario():
    NombreUsuario = input("¿Cómo te llamás? ")
    with open(ArchivoNombre, "w") as Archivo:
        json.dump(NombreUsuario, Archivo)
    return NombreUsuario


def SaludarUsuario():
    NombreUsuario = ObtenerUsuarioGuardado()
    if NombreUsuario:
        Confirmacion = input(f"¿Sos {NombreUsuario}? (s/n): ").lower()
        if Confirmacion == 's':
            print(f"¡Bienvenido de nuevo, {NombreUsuario}!")
        else:
            NombreUsuario = ObtenerNuevoUsuario()
            print(f"¡Te voy a recordar la próxima vez, {NombreUsuario}!")
    else:
        NombreUsuario = ObtenerNuevoUsuario()
        print(f"¡Te voy a recordar la próxima vez, {NombreUsuario}!")


SaludarUsuario()
