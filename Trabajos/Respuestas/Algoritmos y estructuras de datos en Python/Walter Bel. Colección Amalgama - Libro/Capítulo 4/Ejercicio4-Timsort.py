import random
import os
from AlgoritmosOrdenamiento.Mergesort import merge
from AlgoritmosOrdenamiento.Inserctionsort import insercion
os.system('cls')

def timsort(lista):
    min_run = 32  # tamaño mínimo de los bloques6
    n = len(lista)
    # 1. Dividir en bloques (runs) y ordenarlos con inserción
    runs = []
    for i in range(0, n, min_run):
        runs.append(insercion(lista[i:i + min_run]))
    # 2. Combinar runs ordenados de a pares hasta tener la lista completa
    while len(runs) > 1:
        nueva_lista = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                nueva_lista.append(merge(runs[i], runs[i+1]))
            else:
                nueva_lista.append(runs[i])
        runs = nueva_lista
    return runs[0]

lista = [random.randint(0, 100) for _ in range(1000)]
print("Lista original:", lista)
print("Lista ordenada:", timsort(lista))