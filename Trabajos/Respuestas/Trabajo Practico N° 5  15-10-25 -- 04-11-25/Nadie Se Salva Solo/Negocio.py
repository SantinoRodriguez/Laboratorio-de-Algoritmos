import os
os.system('cls')

Stock = [[] for _ in range(10)]
class Hash():
    @staticmethod
    def hash(producto):
        # La función sum produce una sumatoria que simula una repeticion de +=
        return sum(ord(char) for char in producto) % 10

    @staticmethod
    def agregar(producto):
        posicion = Hash.hash(producto)
        bucket = Stock[posicion]
        if (producto not in bucket):
            bucket.append(producto)

    @staticmethod
    def eliminar(producto):
        posicion = Hash.hash(producto)
        bucket = Stock[posicion]
        if (producto in bucket):
            bucket.remove(producto)

Hash.agregar("Jose")
Hash.agregar("Maria")
Hash.agregar("Esteban")
print(Stock)
Hash.eliminar("Jose")
print(Stock)