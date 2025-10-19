import os
import json
os.system('cls')
class Hash():
    @staticmethod
    def hash(producto):
        # La función sum produce una sumatoria que simula una repeticion de +=
        return sum(ord(char) for char in producto) % 10

    @staticmethod
    def agregar(Producto, Precio, Cantidad, Categoria):
        # Leer el archivo JSON existente o crear uno vacío si no existe
        try:
            with open("Stock.json", "r", encoding="utf-8") as Archivo:
                Datos = json.load(Archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            Datos = {"Productos": []}

        # Obtener el código más alto y generar uno nuevo
        if Datos["Productos"]:
            Codigos = [int(Item["Codigo"][1:]) for Item in Datos["Productos"]]
            NuevoCodigo = "C" + str(max(Codigos) + 1).zfill(3)
        else:
            NuevoCodigo = "C001"
        Posicion = Hash.hash(Producto)

        NuevoProducto = {
            "Codigo": NuevoCodigo,
            "Nombre": Producto.title(),
            "Precio": Precio,
            "Cantidad": Cantidad,
            "Categoria": Categoria.title(),
            "Hash": Posicion
        }

        Datos["Productos"].append(NuevoProducto)

        with open("Stock.json", "w", encoding="utf-8") as Archivo:
            json.dump(Datos, Archivo, indent=4, ensure_ascii=False)

        print(f"Producto agregado correctamente: {Producto.title()} ({NuevoCodigo})")

    @staticmethod
    def eliminar(producto):
        Posicion = Hash.hash(producto)
        if (producto in bucket):
            bucket.remove(producto)

Hash.agregar("Batman Comic", 2500, 15, "Dc Comics")
Hash.agregar("Spiderman Comic", 2200, 10, "Marvel Comics")
Hash.agregar("One Piece Volumen 1", 1800, 8, "Manga Japonés")