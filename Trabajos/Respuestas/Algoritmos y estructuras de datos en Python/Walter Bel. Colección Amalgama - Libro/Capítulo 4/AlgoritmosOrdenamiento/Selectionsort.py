def seleccion(lista):
    """Método de ordenamiento selección."""
    """Descripción general:
    Este algoritmo ordena una lista seleccionando en cada pasada
    el elemento más pequeño (o más grande) de la porción no ordenada
    y colocándolo en la posición correcta. 

    El proceso se repite hasta que toda la lista queda ordenada.
    Es sencillo de implementar, pero su complejidad es O(n^2), lo que
    lo hace ineficiente para listas grandes."""
    # Bucle externo: recorre la lista hasta la penúltima posición
    for i in range(0, len(lista) - 1):
        minimo = i   # Se asume que el elemento en la posición i es el menor
        # Bucle interno: busca el elemento más pequeño en la parte no ordenada
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]