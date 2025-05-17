def CiudadPais (Ciudad, Pais, Poblacion=None):
    if Poblacion:
        return f"{Ciudad}, {Pais} – Población {Poblacion}"
    else:
        return f"{Ciudad}, {Pais}"
