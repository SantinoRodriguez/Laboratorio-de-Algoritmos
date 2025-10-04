# Optimizado por ChatGPT para ser mas corto
import time
import random
import os
from AlgoritmosOrdenamiento.Bubblesort import burbuja
from AlgoritmosOrdenamiento.Bubblesort_Mejorado import burbuja_mejorado
from AlgoritmosOrdenamiento.Bubblesort_Birideccional import coctel
from AlgoritmosOrdenamiento.Selectionsort import seleccion
from AlgoritmosOrdenamiento.Inserctionsort import insercion
from AlgoritmosOrdenamiento.Quicksort import quicksort
from AlgoritmosOrdenamiento.Mergesort import mergesort
from AlgoritmosOrdenamiento.Countsort import countsort
os.system('cls')

N = 10000          # tamaño de la lista
MAX_VALUE = 1000  # máximo valor para CountSort
original_list = [random.randint(0, MAX_VALUE) for _ in range(N)]

# Utilidad para medir tiempos
def medir_tiempo(algoritmo, lista, *args):
    arr = lista.copy()
    start = time.time()
    if args:
        resultado = algoritmo(arr, *args)
    else:
        resultado = algoritmo(arr)
    end = time.time()
    return resultado, end - start

# QuickSort
arr = original_list.copy()
_, tiempo = medir_tiempo(quicksort, arr, 0, len(arr) - 1)
print(f"QuickSort tomó {tiempo:.6f} segundos.")

# MergeSort
_, tiempo = medir_tiempo(mergesort, original_list)
print(f"MergeSort tomó {tiempo:.6f} segundos.")

# CountSort
_, tiempo = medir_tiempo(countsort, original_list, MAX_VALUE)
print(f"CountSort tomó {tiempo:.6f} segundos.")

# Burbuja
_, tiempo = medir_tiempo(burbuja, original_list)
print(f"Burbuja tomó {tiempo:.6f} segundos.")

# Burbuja Mejorado
_, tiempo = medir_tiempo(burbuja_mejorado, original_list)
print(f"Burbuja Mejorado tomó {tiempo:.6f} segundos.")

# Cóctel
_, tiempo = medir_tiempo(coctel, original_list)
print(f"Cóctel tomó {tiempo:.6f} segundos.")

# Selección
_, tiempo = medir_tiempo(seleccion, original_list)
print(f"Selección tomó {tiempo:.6f} segundos.")

# Inserción
_, tiempo = medir_tiempo(insercion, original_list)
print(f"Inserción tomó {tiempo:.6f} segundos.")