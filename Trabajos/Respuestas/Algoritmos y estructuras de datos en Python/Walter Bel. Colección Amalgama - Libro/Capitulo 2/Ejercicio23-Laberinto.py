import numpy as np
import random
import os
os.system("cls")

# Generación del laberinto por ChatGPT
def creacion(n):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        laberinto = np.ones((n, n), dtype=int)
        x, y = 0, 0
        laberinto[x, y] = 0
        while x < n-1 or y < n-1:
            if x == n-1:
                y += 1
            elif y == n-1:
                x += 1
            else:
                if random.choice([True, False]):
                    x += 1
                else:
                    y += 1
            laberinto[x, y] = 0

        for i in range(n):
            for j in range(n):
                if laberinto[i, j] != 0:
                    laberinto[i, j] = random.choice([0, 1])

        return laberinto

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

def laberinto(n, x = 0, y = 0, salida = None, visitados = None):
    if salida is None:
        salida = []
    if visitados is None:
        visitados = set()
    if x == len(n) - 1 and y == len(n[0]) - 1:
        salida.append([x, y])
        return salida
    if x < 0 or x >= len(n) or y < 0 or y >= len(n[0]) or n[x][y] == 1:
        return None
    if (x, y) in visitados:
        return None
    visitados.add((x, y))
    salida.append([x, y])
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        camino = laberinto(n, x + dx, y + dy, salida.copy(), visitados.copy())
        if camino is not None:
            return camino
    return None

Esquema = creacion(10)
print("Laberinto generado:\n", Esquema, "\n")
print("Camino encontrado:\n", laberinto(Esquema))