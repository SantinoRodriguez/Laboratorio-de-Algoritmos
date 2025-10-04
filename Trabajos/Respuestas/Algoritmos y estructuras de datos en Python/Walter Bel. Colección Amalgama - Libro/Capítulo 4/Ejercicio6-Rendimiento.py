import random
import time
import os
from AlgoritmosBusqueda.Busqueda_Binaria import binaria
from AlgoritmosBusqueda.Fuerza_Bruta_Centinela import secuencia2
from AlgoritmosBusqueda.Fuerza_Bruta import secuencia
os.system('cls')

# Tamaños de las listas
tamanos = [100_000, 1_000_000, 10_000_000]

# Diccionarios para almacenar las listas y resultados
listas = {}
tiempos = {}

# Generar listas aleatorias
for t in tamanos:
    listas[t] = [random.randint(0, t) for _ in range(t)]

# Función para medir tiempo de ejecución
def medir_tiempo(func, lista, objetivo):
    inicio = time.time()
    resultado = func(lista, objetivo)
    fin = time.time()
    return resultado, fin - inicio

# Probamos cada algoritmo en cada lista
for t in tamanos:
    print(f"\n--- Tamaño de lista: {t:,}".replace(",", ".") + " ---")
    lista = listas[t]
    objetivo = random.choice(lista)  # Seleccionamos un elemento aleatorio para buscar

    # Si es búsqueda binaria, necesitamos lista ordenada
    lista_ordenada = sorted(lista)

    # Búsqueda binaria
    res, tiempo_binaria = medir_tiempo(binaria, lista_ordenada, objetivo)
    print(f"Búsqueda Binaria: elemento {objetivo} {'encontrado' if res is not None else 'no encontrado'}, tiempo: {tiempo_binaria:.6f} s")

    # Fuerza bruta con centinela
    res, tiempo_cent = medir_tiempo(secuencia2, lista, objetivo)
    print(f"Fuerza Bruta Centinela: elemento {objetivo} {'encontrado' if res is not None else 'no encontrado'}, tiempo: {tiempo_cent:.6f} s")

    # Fuerza bruta normal
    res, tiempo_fuerza = medir_tiempo(secuencia, lista, objetivo)
    print(f"Fuerza Bruta Normal: elemento {objetivo} {'encontrado' if res is not None else 'no encontrado'}, tiempo: {tiempo_fuerza:.6f} s")