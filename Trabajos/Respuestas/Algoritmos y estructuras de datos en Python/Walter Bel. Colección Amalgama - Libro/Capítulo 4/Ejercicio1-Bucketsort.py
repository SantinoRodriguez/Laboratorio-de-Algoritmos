import random
import os
from AlgoritmosOrdenamiento.Bubblesort import burbuja
os.system('cls')

def bucket(lista):
    """Método de ordenamiento Bucket Sort (simplificado).
    1. Encuentra mínimo y máximo de la lista.
    2. Divide la lista en cubetas según el rango de valores.
    3. Coloca cada elemento en su cubeta correspondiente.
    4. Ordena cada cubeta individualmente usando burbuja.
    5. Combina las cubetas en la lista final."""

    minimo = lista[0]
    maximo = lista[0]
    lista_ordenada = []

    # Encontrar el mínimo y máximo de la lista
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
        if lista[i] > maximo:
            maximo = lista[i]
    # Definir cantidad de cubetas
    buckets = len(lista) // 5
    # Calcular rango que cubre cada cubeta
    rango = (maximo - minimo + 1) // buckets
    # Crear la lista de cubetas vacías
    cubetas = [[] for _ in range(buckets)]
    # Distribuir los elementos en las cubetas
    for i in lista:
        indice = (i - minimo) // rango
        if indice >= buckets:  # asegurar que el máximo vaya en la última cubeta
            indice = buckets - 1
        cubetas[indice].append(i)
    for i in cubetas:
        burbuja(i)
    # Combinar las cubetas en lista final
    for i in range(1, len(cubetas)):
        if (i % 2 == 1):
            lista_ordenada += cubetas[i - 1] + cubetas[i]
    return f"Lista inicial: {lista}", f"Lista separada en cubetas: {cubetas}", f"Lista final: {lista_ordenada}"

lista = [random.randint(0, 100) for _ in range(20)]
print(*bucket(lista), sep="\n")
