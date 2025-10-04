def burbuja(lista):
    """Método de ordenamiento burbuja."""
    """Descripción general:
    Este algoritmo ordena una lista de elementos de menor a mayor comparando
    elementos adyacentes y cambiándolos de lugar si están en el orden incorrecto.
    Repite este proceso varias veces hasta que toda la lista quede ordenada.
    Es sencillo de implementar, pero no es eficiente para listas grandes
    (complejidad O(n^2))."""
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - i - 1):
            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]