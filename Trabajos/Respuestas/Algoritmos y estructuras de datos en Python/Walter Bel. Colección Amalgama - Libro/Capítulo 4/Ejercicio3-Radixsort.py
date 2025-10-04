import random
import os
from AlgoritmosOrdenamiento.Countsort import countsort
os.system('cls')

def radix(lista):
    mayor = lista[0]
    c = 0
    for i in range(len(lista)):
        if (lista[i] > mayor):
            mayor = lista[i]
    # Cálculo de la cantidad de dígitos del número más grande
    while mayor > 0:
        mayor //= 10
        c += 1
    # Bucle externo: recorre cada dígito desde las unidades hasta el más significativo
    for i in range(1, c + 1):
        for k in range(0, len(lista) - 1):
            for j in range(0, len(lista) - 1):
                # Comparación de los restos módulo
                if (lista[j] % (10 ** i) > lista[j + 1] % (10 ** i)):
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [random.randint(0, 100) for _ in range(20)]
print("Lista original:", lista)
print("Lista ordenada:", radix(lista))

def radixsort(lista):
    """Método de ordenamiento Radix Sort."""
    """Descripción general:
    Radix Sort ordena una lista de números procesando los dígitos de cada número
    desde el menos significativo hasta el más significativo (o al revés, según la implementación).
    En cada pasada, utiliza un algoritmo de ordenamiento estable (como Counting Sort)
    para ordenar los elementos en base al dígito actual.
    
    Su eficiencia es mejor que los métodos simples de comparación (como burbuja o inserción)
    cuando los números tienen pocos dígitos, ya que su complejidad es O(d * (n + k)),
    donde d es la cantidad de dígitos, n el tamaño de la lista y k el rango de los dígitos."""
    # Encontrar el número máximo para saber la cantidad de dígitos
    maximo = max(lista)
    # Aplicar countsort para cada dígito (1, 10, 100, ...)
    exp = 1
    while maximo // exp > 0:
        countsort(lista, exp)
        exp *= 10
    return lista