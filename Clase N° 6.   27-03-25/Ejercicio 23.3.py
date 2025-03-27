def HacerAlbum(Artista, Titulo, CantidadCanciones=None):
    Album = {
        "Artista": Artista,
        "Título": Titulo
    }
    if CantidadCanciones:
        Album["Cantidad De Canciones"] = CantidadCanciones
    return Album

while True:
    Artista = input("Ingresa el nombre del artista (o escribe 'salir' para terminar): ")
    if Artista.lower() == 'salir':
        break
  
    Titulo = input("Ingresa el título del álbum: ")
    
    CantidadCanciones = input("Ingresa la cantidad de canciones (opcional): ")
    if CantidadCanciones:
        CantidadCanciones = int(CantidadCanciones)

    Album = HacerAlbum(Artista.title(), Titulo, CantidadCanciones)
    print("Álbum creado:", Album)
