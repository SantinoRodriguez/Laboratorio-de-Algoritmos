import numpy as np
import os
os.system("cls")

def ajedrez(n, fila = 0, tablero = None, amenazas = None):
    n = 8
    tablero = np.zeros((n, n), dtype=int)
    if tablero is None:
        tablero = []
    if amenazas is None:
        amenazas = set()
    if fila == n:
        return tablero
    for col in range(n):
        if (fila, col) not in amenazas:
            nuevo_tablero = tablero.copy()
            nuevo_tablero.append((fila + 1, col + 1))
            nuevas_amenazas = amenazas.copy()
            for i in range(n):
                nuevas_amenazas.add((fila, i))     
                nuevas_amenazas.add((i, col))   
                if fila + i < n and col + i < n: nuevas_amenazas.add((fila + i, col + i))
                if fila + i < n and col - i >= 0: nuevas_amenazas.add((fila + i, col - i))
                if fila - i >= 0 and col + i < n: nuevas_amenazas.add((fila - i, col + i))
                if fila - i >= 0 and col - i >= 0: nuevas_amenazas.add((fila - i, col - i))

            resultado = ajedrez(n, fila + 1, nuevo_tablero, nuevas_amenazas)
            if resultado is not None:
                return resultado
    return None

print(ajedrez(8))