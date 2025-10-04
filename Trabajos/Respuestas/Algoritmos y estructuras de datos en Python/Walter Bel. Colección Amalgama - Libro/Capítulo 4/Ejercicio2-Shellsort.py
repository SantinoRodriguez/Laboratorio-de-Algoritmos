import random
import os
os.system('cls')

def shell(lista):
    gap = len(lista) // 2
    while gap > 0:
        # Recorremos la lista desde el índice gap hasta el final
        for i in range(gap, len(lista)):
            # Guardamos el valor actual para compararlo
            temp = lista[i]
            # Hacemos insertion sort para elementos separados por gap
            while i >= gap and lista[i - gap] > temp:
                lista[i] = lista[i - gap]  # desplazamos el elemento hacia la derecha
                i -= gap  # retrocedemos según el gap
            lista[i] = temp
        gap //= 2
    return lista

lista = [random.randint(0, 100) for _ in range(20)]
print("Lista original:", lista)
print("Lista ordenada:", shell(lista))