def HacerAlbum(Artista, Titulo, CantidadCanciones = None):
    Album = {"Artista": Artista, "Título": Titulo}
    if CantidadCanciones:
        Album["Cantidad De Canciones"] = CantidadCanciones
    return Album

Album1 = HacerAlbum("Bad Bunny", "YHLQMDLG", 20)
Album2 = HacerAlbum("Karol G", "KG0516", 16)
Album3 = HacerAlbum("J Balvin", "Colores", 10)

print(Album1)
print(Album2)
print(Album3)
